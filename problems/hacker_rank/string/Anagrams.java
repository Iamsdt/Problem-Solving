package hacker_rank.string;

import java.util.Scanner;

class Anagrams {


    public static void main(String[] args) {


        Scanner scan = new Scanner(System.in);
        String a = scan.next();
        String b = scan.next();
        scan.close();
        boolean ret = isAnagram(a, b);
        System.out.println((ret) ? "Anagrams" : "Not Anagrams");

    }

    private static boolean isAnagram(String a, String b) {

        if (a.length() != b.length())
            return false;

        a = a.toLowerCase();
        b = b.toLowerCase();

        int pos = 0;
        for (char c : a.toCharArray()) {
            pos = b.indexOf(c);

            //if not found then pos will be -1
            if (pos == -1) return false;

            //remove char c from string b
            String d = b.substring(0, pos); //from position
            String e = b.substring(pos + 1); // to position
            // and in the gap char c not selected

            b = d+e;
        }


        return true;
    }

}
