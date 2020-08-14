package hacker_rank.month;

import java.util.Scanner;

class Solution {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String firstName = scan.next();
        String lastName = scan.next();
        int id = scan.nextInt();
        int numScores = scan.nextInt();
        int[] testScores = new int[numScores];
        for (int i = 0; i < numScores; i++) {
            testScores[i] = scan.nextInt();
        }
        scan.close();

        Student s = new Student(firstName, lastName, id, testScores);
        s.printPerson();
        System.out.println("Grade: " + s.calculate());
    }


}

class Student extends MPerson {

    private int[] testScores;

    public Student(String firstName, String lastName, int identification,
                   int[] testScores) {
        super(firstName, lastName, identification);
        this.testScores = testScores;
    }


    char calculate() {

        int sum = 0;

        for (int i : testScores) {
            sum = sum + i;
        }

        int total = sum / testScores.length;

        char ch = ' ';

        if (total <= 100 && total >= 90)
            ch = 'O';
        else if (total < 90 && total >= 80)
            ch = 'E';
        else if (total < 80 && total >= 70)
            ch = 'A';
        else if (total < 70 && total >= 55)
            ch = 'P';
        else if (total < 55 && total >= 40)
            ch = 'D';
        else if (total < 40)
            ch = 'T';

        return ch;
    }
}

class MPerson {
    String firstName;
    String lastName;
    int idNumber;

    // Constructor
    MPerson(String firstName, String lastName, int identification) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.idNumber = identification;
    }

    // Print person data
    public void printPerson() {
        System.out.println(
                "Name: " + lastName + ", " + firstName
                        + "\nID: " + idNumber);
    }

}