package hacker_earth.basic_input_output;

import java.util.Scanner;

/**
 * Created by Shudipto on 6/20/2017.
 */
public class Factorial {

    public static void main(String args[]) throws Exception {

        Scanner sc = new Scanner(System.in);
        int cases = sc.nextInt();

        int fact = 1;

        for (int i = 1; i <= cases; i++) {
            fact = fact * i;
        }

        System.out.println(fact);

    }

}
