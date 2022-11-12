package hacker_rank.intro;

import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.GregorianCalendar;
import java.util.Scanner;

//output day name

class DateProblem {

    private static int getInt(String s) {
        return Integer.parseInt(s);
    }

    private static String getDay(String day, String month, String year) {

        Calendar cal = GregorianCalendar.getInstance();
        //month start from zero
        cal.set(getInt(year), getInt(month) - 1, getInt(day));

        SimpleDateFormat format = new SimpleDateFormat("EEEE");

        return format.format(cal.getTime()).toUpperCase();
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String month = in.next();
        String day = in.next();
        String year = in.next();


        System.out.println(getDay(day, month, year));
    }

}
