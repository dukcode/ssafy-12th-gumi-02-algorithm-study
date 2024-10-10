import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class S2817 {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int t;

  private static int n;
  private static int k;
  private static int[] arr;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    t = Integer.parseInt(br.readLine());
    for (int tc = 1; tc <= t; tc++) {

      input();

      bw.write("#" + tc + " ");
      bw.write(String.valueOf(solve(-1, 0)));
      bw.newLine();
    }

    br.close();
    bw.close();

  }

  private static void input() throws IOException {
    st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    k = Integer.parseInt(st.nextToken());

    arr = new int[n];
    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < n; i++) {
      arr[i] = Integer.parseInt(st.nextToken());
    }
  }

  private static int solve(int lastIdx, int sum) {
    if (lastIdx == n - 1) {
      if (sum == k) {
        return 1;
      }

      return 0;
    }

    return solve(lastIdx + 1, sum + arr[lastIdx + 1]) + solve(lastIdx + 1, sum);
  }

}
