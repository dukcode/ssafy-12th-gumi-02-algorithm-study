import java.io.BufferedReader;
import java.io.OutputStreamWriter;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.util.StringTokenizer;

public class B2576 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int sum = 0;
        int min = Integer.MAX_VALUE;
        boolean hasOdd = false;
        for (int i = 0; i < 7; i++) {
            int x = Integer.parseInt(br.readLine());
            
            if (x % 2 == 1) {
                hasOdd = true;
                sum += x;
                min = Math.min(min, x);
            }
        }

        if (hasOdd) {
            bw.write(String.valueOf(sum));
            bw.newLine();
            bw.write(String.valueOf(min));
        } else {
            bw.write("-1");
        }

        br.close();
        bw.close();
    }
}
