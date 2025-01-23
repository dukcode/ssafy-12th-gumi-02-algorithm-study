import java.io.BufferedReader;
import java.io.OutputStreamWriter;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.util.StringTokenizer;

public class B1267 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));


        int n = Integer.parseInt(br.readLine());

        int y = 0;
        int yTotal = 0;
        int m = 0;
        int mTotal = 0;
        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            int y_cost = 0;
            int m_cost = 0;

            int time = Integer.parseInt(st.nextToken());

            if (time <= 29) {
                y_cost += 10;
                m_cost += 15;
            } else if ((time > 30) && (time <= 59)) {
                y_cost += 20;
                m_cost += 15;
            } else {
                y_cost += 10 * ((time / 30) + 1);
                m_cost += 15 * ((time / 60) + 1);
            }

            if (y_cost > m_cost) {
                y++;
            } else if (y_cost == m_cost) {
                y++;
                m++;
            } else {
                m++;
            }
            yTotal += y_cost;
            mTotal += m_cost;

        }
        if (y < m) {
            bw.write("Y" + " " + String.valueOf(yTotal));
        } else if (y == m) {
            bw.write("Y" + " " + "M" + " " + String.valueOf(mTotal));
        } else {
            bw.write("M" + " " + String.valueOf(mTotal));
        }

        br.close();
        bw.close();

    }
}
