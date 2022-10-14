package hacker_rank.month;

import java.util.Arrays;
import java.util.Scanner;

public class Day252 {

    public static void main(String[] args){

        Scanner scanner = new Scanner(System.in);

        int i = scanner.nextInt();

        for (int j = 0; j < i; j++) {
            int k = scanner.nextInt();
            if (isPrime(k)){
                System.out.println("Prime");
            } else System.out.println("Not prime");
        }

    }

    public static boolean isPrime(int n){
        if(n == 1){
            return false;
        }
        if(n == 2){
            return true;
        }
        for (int i = 2; i*i<=n; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }

}
