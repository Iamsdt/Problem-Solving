package implementation;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class ArrayInsert {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String a[] = br.readLine().split(" ");

        int N = Integer.parseInt(a[0]);
        int Q = Integer.parseInt(a[1]);

        String array = br.readLine();

        int ar[] = Arrays.stream(array.split(" ")).mapToInt(Integer::parseInt).toArray();

        String q[];

        for (int i = 0; i < Q; i++) {
            q = br.readLine().split(" ");
            if (Integer.parseInt(q[0]) == 1) {
                ar[Integer.parseInt(q[1])] = Integer.parseInt(q[2]);
            } else {
                int sum = 0;
                for (int j = Integer.parseInt(q[1]); j <= Integer.parseInt(q[2]); j++)
                    sum += ar[j];
                System.out.println(sum);
            }
        }
        br.close();
    }
}
