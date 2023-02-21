class widget
{
private:
    gadget g; // lifetime automatically tied to enclosing object
public:
    void draw();
};

void functionUsingWidget()
{
    widget w; // lifetime automatically tied to enclosing scope
              // constructs w, including the w.g gadget member
    // ...
    w.draw();
    // ...
} // automatic destruction and deallocation for w and w.g
  // automatic exception safety,
  // as if "finally { w.dispose(); w.g.dispose(); }"