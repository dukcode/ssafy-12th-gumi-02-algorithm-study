import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

// 수영장
public class S1952 {

  private static final int MX = 987_654_321;

  private static final int NUM_MONTH = 12;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int t;
  private static int[] costs;
  private static int[] days;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    t = Integer.parseInt(br.readLine());
    for (int tc = 1; tc <= t; tc++) {
      costs = new int[4];
      st = new StringTokenizer(br.readLine());
      for (int i = 0; i < 4; i++) {
        costs[i] = Integer.parseInt(st.nextToken());
      }

      days = new int[NUM_MONTH];
      st = new StringTokenizer(br.readLine());
      for (int i = 0; i < NUM_MONTH; i++) {
        days[i] = Integer.parseInt(st.nextToken());
      }

      bw.write("#" + tc + " ");
      bw.write(String.valueOf(Math.min(costs[3], solve(0, 0))));
      bw.newLine();
    }

    br.close();
    bw.close();

  }

  private static int solve(int month, int money) {
    if (month >= 12) {
      return money;
    }

    int ret = solve(month + 1, money + days[month] * costs[0]);
    ret = Math.min(ret, solve(month + 1, money + costs[1]));
    ret = Math.min(ret, solve(month + 3, money + costs[2]));
    return ret;
  }

}
