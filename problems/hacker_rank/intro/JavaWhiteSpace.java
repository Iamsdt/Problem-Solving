package hacker_rank.intro;

import java.util.Scanner;

class JavaWhiteSpace {

    public static void main(String[] arg) {

        Scanner sc = new Scanner(System.in);
        System.out.println("================================");
        for (int i = 0; i < 3; i++) {
            String s1 = sc.next();
            int x = sc.nextInt();


            StringBuilder sb = new StringBuilder();
            sb.append(s1);
            int start = s1.length();
            while (start < 15){
                sb.append(" ");
                start++;
            }

            if (x < 100){
                sb.append(0);
                if (x < 10){
                    sb.append(0);
                }
            }
            sb.append(x);
            System.out.println(sb.toString());
        }
        System.out.println("================================");

    }

}
