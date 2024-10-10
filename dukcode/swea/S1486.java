import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

// 장훈이의 높은 선반
public class S1486 {

  private static final int MX = 987_654_321;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int t;

  private static int n;
  private static int b;

  private static int[] h;

  private static int minHeight;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    t = Integer.parseInt(br.readLine());
    for (int tc = 1; tc <= t; tc++) {
      st = new StringTokenizer(br.readLine());
      n = Integer.parseInt(st.nextToken());
      b = Integer.parseInt(st.nextToken());

      h = new int[n];
      st = new StringTokenizer(br.readLine());
      for (int i = 0; i < n; i++) {
        h[i] = Integer.parseInt(st.nextToken());
      }

      minHeight = MX;
      solve(-1, 0);

      bw.write("#" + tc + " ");
      bw.write(String.valueOf(minHeight - b));
      bw.newLine();
    }

    br.close();
    bw.close();

  }

  private static void solve(int lastIdx, int sum) {
    if (lastIdx == n - 1) {
      if (sum < b) {
        return;
      }
      minHeight = Math.min(minHeight, sum);
      return;
    }

    if (sum > minHeight) {
      return;
    }

    solve(lastIdx + 1, sum);
    for (int nextIdx = lastIdx + 1; nextIdx < n; nextIdx++) {
      solve(nextIdx, sum + h[nextIdx]);
    }
  }

}
