import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.io.IOException;
import java.util.StringTokenizer;

public class B2752 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int x = Integer.parseInt(st.nextToken());
        int y = Integer.parseInt(st.nextToken());
        int z = Integer.parseInt(st.nextToken());

        int[] data = new int[]{x, y, z};
        for (int i = 0; i < 2; i++) {
            int num;
            for (int j = i+1; j <= 2; j++) {
            if (data[i] > data[j]) {
                num = data[j];
                data[j] = data[i];
                data[i] = num;
            }
            }
        }

        for (int i = 0; i < 3; i++) {
            if (i == 2) {
                bw.write(data[i] + "");
            } else {
                bw.write(data[i] + " ");
            }
            }
        bw.close();
    }


    }
