package hacker_rank;

import java.util.Scanner;
import java.util.regex.Pattern;

class JavaTest {

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int testCases = Integer.parseInt(in.nextLine());
        while (testCases > 0) {
            String pattern = in.nextLine();

            try {
                Pattern.compile(pattern);
                System.out.println("Valid");
            } catch (Exception e){
                System.out.println("No Valid");
            }



            testCases++;
        }
    }
}