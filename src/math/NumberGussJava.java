package math;

import java.util.Scanner;

class NumberGussJava {
    public static void main(String[] arg){
        Scanner scanner = new Scanner(System.in);

        int times = scanner.nextInt();

        for (int i = 0; i < times; i++) {
            int sum = 0;
            int number = scanner.nextInt();

            for (int j = 1; j < number; j++) {
                if (number % j == 0) sum += j;
            }

            System.out.println(sum);
        }
    }

}
