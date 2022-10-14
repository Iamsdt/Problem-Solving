package hacker_rank.month;

import java.util.Scanner;

public class Person {
    private int age;

    public Person(int initialAge) {
        if (initialAge > 0){
            age = initialAge;
        } else {
            System.out.println("Age is not valid, setting age to 0.");
        }
    }

    public void amIOld() {
        String s = "";

        if (age < 13){
            s = "You are young.";
        } else if (age >= 13 && age <18){
            s = "You are a teenager.";
        } else {
            s = "You are old.";
        }


        System.out.println(s);
    }

    public void yearPasses() {
        age++;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        for (int i = 0; i < T; i++) {
            int age = sc.nextInt();
            Person p = new Person(age);
            p.amIOld();
            for (int j = 0; j < 3; j++) {
                p.yearPasses();
            }
            p.amIOld();
            System.out.println();
        }
        sc.close();
    }
}
