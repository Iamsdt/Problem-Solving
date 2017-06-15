package basic_input_output;
import java.util.Scanner;

/**
 * Created by Shudipto Trafder on 6/15/2017.
 */
public class ToggleString {

    /**
     * You have been given a String
     S consisting of uppercase and lowercase English alphabets. You need to change the case of each alphabet in this String. That is, all the uppercase letters should be converted to lowercase and all the lowercase letters should be converted to uppercase. You need to then print the resultant String to output.

     Input Format
     The first and only line of input contains the String

     Output Format
     Print the resultant String on a single line.

     like aBcDe AbCdE
     * **/



    public static void main(String args[]) throws Exception {

        Scanner scanner = new Scanner(System.in);

        String s = scanner.next();

        StringBuilder stringBuilder = new StringBuilder();

        for (int i = 0; i < s.length(); i++) {

            char c = s.charAt(i);

            if (Character.isLowerCase(c)){
                stringBuilder.append(Character.toUpperCase(c));

            } else if (Character.isUpperCase(c)){
                stringBuilder.append(Character.toLowerCase(c));
            }
        }

        System.out.print(stringBuilder.toString());

    }
}
