package math;

import java.util.Scanner;

class LoveTriangleJava {

    public static void main(String[] arg) {
        Scanner scanner = new Scanner(System.in);
        int num = scanner.nextInt();
        System.out.println(find(num));
    }

    static int find(int number) {
        if (number < 9) return number;
        else return number % 9 + 10 * find(number / 9);
    }
}