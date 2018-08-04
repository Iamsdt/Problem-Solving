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

/*
Find the logic from the given sample input/output.

And answer Q queries.

Constraints :

1 <= Value <= 100000
1<=nunber of query<=10000

SAMPLE INPUT   SAMPLE OUTPUT
8
10  8
30  42
45  33
9   4
69  27
77  19
127 1
150 222
 */
