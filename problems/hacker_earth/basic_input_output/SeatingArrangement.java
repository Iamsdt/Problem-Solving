package hacker_earth.basic_input_output;

import java.util.Scanner;

/**
 * Created by Shudipto Trafder on 6/16/2017.
 */
public class SeatingArrangement {

    public static void main(String args[]) throws Exception {

        Scanner sc = new Scanner(System.in);
        int cases = sc.nextInt();
        int num;
        for (int i = 0; i < cases; i++) {
            int seatNo = sc.nextInt();
            int mod = seatNo % 12;
            switch (mod) {
                //for ws 0 1 6 7
                case 1:
                    num = seatNo != 1 ? seatNo + 11 : 12;
                    System.out.println(num + " " + "WS");
                    break;
                case 6:
                    num = seatNo != 6 ? seatNo + 1 : 7;
                    System.out.println(num + " " + "WS");
                    break;
                case 7:
                    num = seatNo != 7 ? seatNo - 1 : 6;
                    System.out.println(num + " " + "WS");
                    break;
                case 0:
                    num = seatNo != 12 ? seatNo - 11 : 1;
                    System.out.println(num + " " + "WS");
                    break;

                //for ms 2, 5 8 11
                case 2:
                    num = seatNo != 2 ? seatNo + 9 : 11;
                    System.out.println(num + " " + "MS");
                    break;
                case 5:
                    num = seatNo != 5 ? seatNo + 3 : 8;
                    System.out.println(num + " " + "MS");
                    break;
                case 8:
                    num = seatNo != 8 ? seatNo - 3 : 5;
                    System.out.println(num + " " + "MS");
                    break;
                case 11:
                    num = seatNo != 11 ? seatNo - 9 : 2;
                    System.out.println(num + " " + "MS");
                    break;

                //for as 3 4 9 10
                case 3:
                    num = seatNo != 3 ? seatNo + 7 : 10;
                    System.out.println(num + " " + "AS");
                    break;
                case 4:
                    num = seatNo != 4 ? seatNo + 5 : 9;
                    System.out.println(num + " " + "AS");
                    break;
                case 9:
                    num = seatNo != 9 ? seatNo - 5 : 4;
                    System.out.println(num + " " + "AS");
                    break;
                case 10:
                    num = seatNo != 10 ? seatNo - 7 : 3;
                    System.out.println(num + " " + "AS");
                    break;

            }
        }
    }
    //problem link
    /*
    Akash and Vishal are quite fond of travelling.
     They mostly travel by railways.
      They were travelling in a train one day and they got
      interested in the seating arrangement of their compartment.
       The compartment looked something like

       So they got interested to know the seat number facing them
       and the seat type facing them. The seats are denoted as follows :
        Window Seat : WS
        Middle Seat : MS
        Aisle Seat : AS

        You will be given a seat number, find out the seat
        number facing you and the seat type, i.e. WS, MS or AS.
    */
}
