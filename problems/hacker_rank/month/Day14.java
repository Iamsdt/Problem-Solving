package hacker_rank.month;

import java.util.Scanner;

class Day14 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }
        sc.close();

        Difference difference = new Difference(a);

        difference.computeDifference1();

        System.out.print(difference.maximumDifference);
    }

}

class Difference {
    private int[] elements;
    public int maximumDifference;

    Difference(int[] a) {
        elements = a;
        maximumDifference = 0;
    }

    //O (n2)
    public void computeDifference() {

        //1 5 6 8

        for (int element : elements) {

            for (int element1 : elements) {

                int c = element - element1;

                c = Math.abs(c);

                if (c > maximumDifference) {
                    maximumDifference = c;
                }
            }
        }
    }

    //O(n)

    int min = Integer.MAX_VALUE;
    int max = 0;

    public void computeDifference1() {

        //1 5 6 8

        for (int element : elements) {
            if (min > element) min = element;
            if (max < element) max = element;
        }

        maximumDifference = max - min;
    }
}


