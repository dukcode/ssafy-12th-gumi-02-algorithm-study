import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class MinNumOfJumps {

  private static final int MX = 987_654_321;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int[] arr;

  private static int ans;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    n = Integer.parseInt(br.readLine());

    arr = new int[n];
    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < n; ++i) {
      arr[i] = Integer.parseInt(st.nextToken());
    }

    ans = MX;
    solve(n - 1, 0);

    bw.write(String.valueOf(ans == MX ? -1 : ans));

    br.close();
    bw.close();

  }

  private static void solve(int now, int cnt) {
    if (now == 0) {
      ans = Math.min(ans, cnt);
      return;
    }

    if (ans <= cnt) {
      return;
    }

    for (int step = 1; step <= 4; ++step) {
      int before = now - step;
      if (before < 0 || arr[before] < step) {
        continue;
      }

      solve(before, cnt + 1);
    }
  }

}
