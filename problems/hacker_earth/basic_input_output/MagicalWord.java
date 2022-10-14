package hacker_earth.basic_input_output;

import java.util.Scanner;

/**
 * Created by Shudipto Trafder on 6/20/2017.
 */
public class MagicalWord {

    private static String checkStringLength(String str, int length) {
        Scanner newString = new Scanner(System.in);
        while (str.length() > length) {
            str = newString.nextLine();
        }
        return str;
    }

    private static int checkIntLength(int value, int min, int max) {
        Scanner newString = new Scanner(System.in);
        while (value < min || value > max) {
            value = newString.nextInt();
        }
        return value;
    }

    public static void main(String[] args) {

        int T, N, start = 0, end = 0, prevPoint = 0, nextPoint;
        int j, k, diff1, diff2, point, result = 0;

        String str;

        Scanner scanner = new Scanner(System.in);

        T = scanner.nextInt();

        T = checkIntLength(T, 1, 100);



        for (int i = 0; i < T; i++) {
            N = scanner.nextInt();
            N = checkIntLength(N, 1, 500);
            str = scanner.next();
            str = checkStringLength(str, N);
            for (int m = 0; m < str.length(); m++) {
                char ch = str.charAt(m);
                if (ch >= 'A' && ch <= 'Z' || ch >= 'a' && ch <= 'z') {
                    point = ch;
                    if (ch >= 'A' && ch <= 'Z') {
                        start = 65;
                        end = 90;
                    }
                    if (ch >= 'a' && ch <= 'z') {
                        start = 97;
                        end = 122;
                    }
                    for (j = start; j < point; j++) {
                        for (k = 2; k <= j; k++) {
                            if (j % k == 0)
                                break;
                        }
                        if (j == k)
                            prevPoint = j;
                    }
                    for (j = point; j <= end; j++) {
                        for (k = 2; k <= j; k++) {
                            if (j % k == 0)
                                break;
                        }
                        if (j == k) {
                            nextPoint = j;
                            diff1 = point - prevPoint;
                            diff2 = nextPoint - point;
                            if (diff1 <= diff2)
                                result = prevPoint;
                            else
                                result = nextPoint;
                            break;
                        }
                    }
                    if (result == 0)
                        str = str.replace(ch, (char) (prevPoint));
                    str = str.replace(ch, (char) (result));
                    result = prevPoint = 0;
                } else if (ch < 65)
                    str = str.replace(ch, (char) (67));
                else if (ch > 93 && ch < 122)
                    str = str.replace(ch, (char) (97));
                else if (ch > 122)
                    str = str.replace(ch, (char) (113));
                else if (ch > 90 && ch < 94)
                    str = str.replace(ch, (char) (89));

            }
            System.out.println(str);
        }
    }

    /*
    * Dhananjay has recently learned about ASCII values.He is very fond of
    * experimenting. With his knowledge of ASCII values and character he has
    * developed a special word and named it Dhananjay's Magical word.
    * A word which consist of alphabets whose ASCII values is a prime number
    * is an Dhananjay's Magical word. An alphabet is Dhananjay's Magical alphabet
     * if its ASCII value is prime.
     *
     * Dhananjay's nature is to boast about the things he know or have learnt
     * about. So just to defame his friends he gives few string to his friends
     * and ask them to convert it to Dhananjay's Magical word. None of his friends
      * would like to get insulted. Help them to convert the given strings to
       * Dhananjay's Magical Word.
       *
       * Rules for converting:
       *
       * 1.Each character should be replaced by the nearest Dhananjay's Magical alphabet.
       * 2.If the character is equidistant with 2 Magical alphabets.
        * The one with lower ASCII value will be considered as its replacement.
        *
        * Input format:
        *
        * First line of input contains an integer T number of test cases.
         * Each test case contains an integer N (denoting the length of the string) and a string S.
        * Output Format:
        *
        * For each test case, print Dhananjay's Magical Word in a new line.
        *
        * SAMPLE INPUT
        * 1
        * 6
        * AFREEN
        *
        * SAMPLE OUTPUT
        *
        * CGSCCO
    * */
}
