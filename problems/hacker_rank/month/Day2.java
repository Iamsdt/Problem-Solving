package hacker_rank.month;

import java.util.Scanner;

class Day2 {
    public static void main(String[] arg) {
        int i = 4;
        double d = 4.0;
        String s = "HackerRank ";

        Scanner scan = new Scanner(System.in);

        int v = scan.nextInt();
        scan.nextLine();
        double de = scan.nextDouble();
        scan.nextLine();
        String string = scan.nextLine();

        double r = d + de;

        r = Math.round(r * 10.0) / 10.0;

        System.out.println(i+v);
        System.out.println(r);
        System.out.println(s+string);

    }

}
