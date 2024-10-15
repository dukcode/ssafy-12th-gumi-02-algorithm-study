import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BeingRichByWorkingPartTime {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int[] s;
  private static int[] e;
  private static int[] p;

  private static int[] cache;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    n = Integer.parseInt(br.readLine());

    s = new int[n];
    e = new int[n];
    p = new int[n];
    for (int i = 0; i < n; i++) {
      st = new StringTokenizer(br.readLine());
      s[i] = Integer.parseInt(st.nextToken());
      e[i] = Integer.parseInt(st.nextToken());
      p[i] = Integer.parseInt(st.nextToken());
    }

    cache = new int[n + 1];
    Arrays.fill(cache, -1);
    bw.write(String.valueOf(solve(-1)));

    br.close();
    bw.close();

  }

  private static int solve(int idx) {
    if (idx == n - 1) {
      return cache[idx + 1] = p[idx];
    }

    if (cache[idx + 1] != -1) {
      return cache[idx + 1];
    }

    int pNow = idx == -1 ? 0 : p[idx];
    int ret = pNow;
    for (int i = idx + 1; i < n; i++) {
      if (idx != -1 && e[idx] >= s[i]) {
        continue;
      }

      ret = Math.max(ret, solve(i) + pNow);
    }

    return cache[idx + 1] = ret;
  }

}
