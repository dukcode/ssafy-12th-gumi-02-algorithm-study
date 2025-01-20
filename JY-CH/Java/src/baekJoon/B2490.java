import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.io.IOException;
import java.util.Arrays;
import java.util.StringTokenizer;

public class B2490 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));


        for (int i = 0; i < 3; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int cnt = 0;
            for (int idx = 0; idx < 4; idx++) {
                int num = Integer.parseInt(st.nextToken());
                if (num == 0) {
                    cnt++;
                }
            }
            if (cnt == 1) {
                bw.write("A" + "\n");
            } else if (cnt == 2) {
                bw.write("B" + "\n");
            } else if (cnt == 3) {
                bw.write("C" + "\n");
            } else if (cnt == 4) {
                bw.write("D" + "\n");
            } else {
                bw.write("E" + "\n");
            }

        }
        br.close();
        bw.close();




    }
}
