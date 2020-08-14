package hacker_earth.basic_input_output;

import java.util.Scanner;

/**
 * Created by Shudipto Trafder on 6/20/2017.
 */

public class CountDivisor {


    public static void main(String args[]) throws Exception {

        Scanner sc = new Scanner(System.in);
        int l = sc.nextInt();
        int r = sc.nextInt();
        int k = sc.nextInt();

        int count = 0;

        for (; l <= r; l++) {

            if ((l % k) == 0) {
                count++;

            }
        }

        System.out.println(count);

    }
}
