package hacker_rank.string;

import java.util.Scanner;

class FormatString {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String A = sc.next();
        String B = sc.next();

        int len = A.length() + B.length();
        System.out.println(len);

        char av = A.charAt(0);
        char bv = B.charAt(0);

        if (av > bv) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }

        String s = A.substring(0, 1);
        String s2 = B.substring(0, 1);

        A = A.replaceFirst(s, s.toUpperCase());
        B = B.replaceFirst(s2, s2.toUpperCase());

        System.out.println(A + " " + B);
    }

}
