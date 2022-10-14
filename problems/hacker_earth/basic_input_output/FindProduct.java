package hacker_earth.basic_input_output;

import java.util.Scanner;

/**
 * Created by Shudipto Trafder on 6/20/2017.
 */
public class FindProduct {

    public static void main(String args[]) throws Exception {

        Scanner sc = new Scanner(System.in);
        int size = sc.nextInt();

        int[] array = new int[size];

        long mod = 1000000007;

        long ans = 1;

        for (int i = 0; i <= size-1; i++) {
            array[i] = sc.nextInt();
            ans = (ans * array[i]) % mod;
        }

        System.out.println(ans);
    }
}
