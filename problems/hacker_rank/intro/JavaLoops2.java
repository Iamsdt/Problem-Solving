package hacker_rank.intro;

import java.util.Scanner;

class JavaLoops2 {

    public static void main(String[] argh) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for (int i = 0; i < t; i++) {
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();

            //do
            int res = a;
            for (int j = 0; j < n; j++) {
                res += (int) (Math.pow(2.0, j) * b);
                System.out.print(res + " ");
            }


        }
        in.close();
    }

}
