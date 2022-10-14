package hacker_rank.month;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

class Day8 {

    public static void main(String[] arg){

        Map<String,Integer> map = new HashMap<>();

        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        for(int i = 0; i < n; i++){
            String name = in.next();
            int phone = in.nextInt();
            // Write code here
            map.put(name,phone );
        }
        while(in.hasNext()){
            String s = in.next();
            if (map.containsKey(s)){
                System.out.println(s+"="+map.get(s));
            } else {
                System.out.println("Not found");
            }
        }
        in.close();

    }

}
