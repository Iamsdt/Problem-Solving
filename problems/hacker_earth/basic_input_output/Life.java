package hacker_earth.basic_input_output;

import java.util.Scanner;

public class Life {

    public static void main(String[] arg){

        Scanner scanner = new Scanner(System.in);

        while (true){
            int i = scanner.nextInt();

            if (i == 42){
                break;
            } else {
                System.out.println(i);
            }
        }

    }

}
