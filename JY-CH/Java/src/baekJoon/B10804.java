import java.io.BufferedReader;
import java.io.OutputStreamWriter;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.util.StringTokenizer;

public class B10804 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int[] numbers = new int[20];
        for (int i = 0; i < 20; i++) {
            numbers[i] = i+1;
        }

        int count = 10;
        for (int i = 0; i < 10; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());

            for (int j = 0; j < (end - start + 1) / 2; j++) {
                int tmp = numbers[start-1 + j];
                numbers[start-1+j] = numbers[end-1-j];
                numbers[end-1-j] = tmp;
            }
        }

        for (int i = 0; i < numbers.length; i++) {
            bw.write(numbers[i] + " ");
        }
        br.close();
        bw.close();

    }
}
