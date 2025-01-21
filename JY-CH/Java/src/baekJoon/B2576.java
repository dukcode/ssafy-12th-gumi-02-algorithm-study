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



        int answer_sum = 0;
        int minimum = Integer.MAX_VALUE;
        for (int i = 0; i < 7; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());

            if (x % 2 == 1) {
                answer_sum += x;
                if (minimum > x) {
                    minimum = x;
                }
            }
        }

        if (answer_sum != 0) {
            bw.write(answer_sum + "\n" + minimum);
        } else {
            bw.write("-1");
        }

        br.close();
        bw.close();
    }
}
