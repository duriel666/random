internal class CrystalTree
{
    private const uint growingState = 0x0, splittingState = 0x1, finishedState = 0x2;
    private const uint hasParentFlag = 0x10;
    private const uint stateMask = 0xf;

    #region Types

    internal struct CrystalGrowthBehavior : IEntityBehavior<TickEvent>
    {
        private static readonly ThreadLocal<Random> tlr = new(() => new());

        public void Post(in BehaviorArgument arg, in TickEvent e)
        {
            var world = (EntityWorld_)arg.world;                        // EntityWorld_ is a prototype version of IEntityWorld, interface will be used directly when it settles
            var bSys = arg.behaviors;
            var tSys = world.server.RequireService<TransformSystem>();
            var cSys = world.server.RequireService<ComponentSystem>();  // Get necessary services
            var time = world.server.RequireService<TimeService>();
            var rand = tlr.Value;

            var curTime = time.time;
            foreach (var id in arg.ids)
            {
                var ct = cSys.RequireTyped<CrystalTree>(id);            // Extension method to use type as column attribute
                var t = tSys.GetTransform(id);
                var pt = ct.parentId != null ? tSys.GetTransform(ct.parentId.Value) : null;

                if (ct.state == growingState)
                {
                    var initialScale = pt?.scale ?? Vec3.one;
                    var finalScale = initialScale * ct.pattern_.growthFactor_;

                    var gFac = MathF.Min(1, (curTime - ct.birthDate_) / ct.pattern_.generationPeriod_); // Interpolate scale

                    t.scale = VecN.Lerp(Vec3.Fill(0.0001f), finalScale, gFac);

                    var spawnTime = ct.birthDate_ + ct.pattern_.generationPeriod_;
                    if (curTime >= spawnTime)
                    {
                        ct.state = splittingState;      // Transition state
                    }
                }

                if (ct.state == splittingState)
                {
                    if (ct.generation_ < ct.pattern_.maxGeneration_)
                    {          // Create children
                        for (int i = 0; i < ct.pattern_.childCount_; i++)
                        {
                            New_(world, ct.pattern_, id, rand, ct.generation_ + 1, curTime);
                        }
                    }

                    ct.state = finishedState;
                }

                if (ct.state == finishedState)
                {
                    bSys.RemoveBehavior(id, instance); // Growth is over, disable the behavior
                }
            }
        }

        public static readonly IEntityBehavior<TickEvent> instance = new CrystalGrowthBehavior();
    }

    internal class Pattern
    {
        internal EntityRenderable renderable_; // A model+shader combo that can be associated with entities
        internal int maxGeneration_;
        internal float generationPeriod_;
        internal float growthFactor_; // Relative size of children
        internal int childCount_;
    }

    #endregion Types

    #region Internal

    private uint state
    {
        get => flags_ & stateMask;
        set => flags_ = (flags_ & ~stateMask) | value;
    }

    private EntityId? parentId => (flags_ & hasParentFlag) == hasParentFlag ? parentId_ : null;

    private static EntityId New_(EntityWorld_ world, Pattern pattern, EntityId? parent, Random? random, int generation, float time)
    {
        var bSys = world.server.RequireService<BehaviorSystem>();
        var cSys = world.server.RequireService<ComponentSystem>(); // Get required services
        var tSys = world.server.RequireService<TransformSystem>(); // Each service is entirely modular and separable
        var rSys = world.server.RequireService<RenderSystem>();

        var eId = world.New(0);

        cSys.SetTyped(eId, new CrystalTree(pattern, time, parent, generation)); // Add our new crystal tree entry using type as the column attribute

        var t = tSys.EnsureTransform(eId);
        if (parent != null)
        {
            var pt = tSys.GetTransform(parent.Value);

            Quaternion rotOffset;
            if (random != null)
            {
                var axisOffset = VecN.Norm(new Vec3(VecN.Lerp(-1f, 1f, (float)random.NextDouble()),
                    VecN.Lerp(-1f, 1f, (float)random.NextDouble()), 0.1f));

                rotOffset = Quaternion.AngleAxis(axisOffset, 0.2f); // Tilt a little
            }
            else
            {
                rotOffset = Quaternion.identity;
            }

            t.rotation = pt.rotation * rotOffset;
            t.position = MatN.TransformFast(pt.matrixOut, Quaternion.Rotate(rotOffset, new Vec3(0, 1, 0))); // Offset from parent
            t.scale = Vec3.Fill(0.0001f);
        }

        rSys.SetRenderable(eId, pattern.renderable_); // Add our renerable

        bSys.AddBehavior(eId, CrystalGrowthBehavior.instance); // Add our behavior
        return eId;
    }

    #endregion Internal

    public static EntityId New(EntityWorld_ world, Pattern pattern)
    {
        var tSys = world.server.RequireService<TimeService>();
        return New_(world, pattern, null, null, 0, tSys.time);
    }

    internal CrystalTree(Pattern pattern, float time, EntityId? parentId, int generation)
    {
        parentId_ = parentId ?? default;
        pattern_ = pattern;
        generation_ = generation;
        birthDate_ = time;
        flags_ = (parentId != null ? growingState | hasParentFlag : splittingState);
    }

    #region Fields

    private readonly EntityId parentId_;
    private readonly Pattern pattern_;
    private readonly int generation_;
    private readonly float birthDate_;
    private uint flags_;

    #endregion Fields
}