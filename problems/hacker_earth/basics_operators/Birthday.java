package hacker_earth.basics_operators;

import java.util.Scanner;

public class Birthday {

    public static void main(String[] arg) {
        Scanner br = new Scanner(System.in);
        int tCases = br.nextInt();
        while (tCases > 0) {
            int friends = br.nextInt();
            int chocolates = br.nextInt();
            if ((chocolates % friends) == 0) {
                System.out.println("Yes");
            } else {
                System.out.println("No");
            }
            tCases--;
        }
    }
}
