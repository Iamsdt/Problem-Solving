package implementation;

import java.util.Scanner;

public class ShittyFortune {

    public static void main(String[] arg){
        String str;
        StringBuilder rev = new StringBuilder();

        Scanner sc = new Scanner(System.in);

        int time = sc.nextInt();

        for (int i = 0; i < time; i++) {

            str = sc.nextLine();

            int length = str.length();

            for ( int j = length - 1; j >= 0; j-- )
                rev.append(str.charAt(j));

            if (str.equals(rev.toString()))
                System.out.println("YES");
            else
                System.out.println("NO");
        }
    }

}
