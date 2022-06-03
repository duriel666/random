import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /*
         * Enter your code here. Read input from STDIN. Print output to STDOUT. Your
         * class should be named Solution.
         */
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        sc.close();
        int x = 0;
        for (int i = 0; i < s.length() / 2; i++) {
            if (s.charAt(i) != s.charAt(s.length() - i - 1)) {
                x += 1;
            }
        }
        if (x == 0) {
            System.out.println("Yes");
        }
        else{
            System.out.println("No");
        }
    }
}
