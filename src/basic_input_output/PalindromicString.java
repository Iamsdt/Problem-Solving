package basic_input_output;

import java.util.Scanner;

/**
 * Created by Shudipto on 6/15/2017.
 */
public class PalindromicString {

    //problems
    /*
    * You have been given a String
    * You need to find and print whether this string
    * is a palindrome or not.
    * If yes, print "YES" (without quotes),
    * else print "NO" (without quotes).
    * sample- abc -> yes*/

    /* palindrome is a word, phrase, or sequence
     * that reads the same backward as forward,
     * e.g., madam or nurses run.
     */

    public static void main(String args[]) throws Exception {

        Scanner scanner = new Scanner(System.in);
        String s = scanner.next();

        char[] chars = null;

        for (int i = 0; i < s.length(); i++) {
            chars = new char[]{s.charAt(i)};
        }

        if (instPalindrome(chars)) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }

        System.out.println("New result");
        if (check(s)){
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }
    }

    //that's show error result for long string
    private static boolean instPalindrome(char[] word) {

        int i1 = 0;
        int i2 = word.length - 1;

        while (i2 > i1) {
            if (word[i1] != word[i2]) {
                return false;
            }
            ++i1;
            --i2;
        }
        return true;
    }

    private static boolean check(String s){
        int i1 = 0;
        int i2 = s.length() - 1;

        while (i2 > i1){
            if (s.charAt(i1) != s.charAt(i2)){
                return false;
            }
            ++i1;
            --i2;
        }
        return true;
    }

}
