package hacker_rank.string;

import java.util.Scanner;

class StringSplit {

    /*
    Given a string, , matching the regular expression [A-Za-z !,?._'@]+, split the string into tokens. We define a token to be one or more consecutive English alphabetic letters. Then, print the number of tokens, followed by each token on a new line.
     */

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {

        String s = scanner.nextLine();

        s = s.trim();

        if (s.length() == 0) {
            System.out.println(s.length());
        } else if (s.length() < 400000) {
            String[] temp = s.split("[ !,?.\\_'@]");

            System.out.println(temp.length);
            for (String aTemp : temp) {
                System.out.println(aTemp);
            }
        }
    }

}
