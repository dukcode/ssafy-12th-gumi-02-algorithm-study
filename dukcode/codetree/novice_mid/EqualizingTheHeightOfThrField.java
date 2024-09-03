import java.util.*;
import java.io.*;

public class EqualizingTheHeightOfThrField {
  private static final int MX = 987_654_321;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int h;
  private static int t;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(br.readLine());
    h = Integer.parseInt(br.readLine());
    t = Integer.parseInt(br.readLine());

    int[] psum = new int[n + 1];
    st = new StringTokenizer(br.readLine());
    for (int i = 1; i <= n; ++i) {
      psum[i] = psum[i - 1] + Math.abs(h - Integer.parseInt(st.nextToken()));
    }

    int minCost = MX;
    for (int st = 0; st <= n - t; ++st) {
      minCost = Math.min(minCost, psum[st + t] - psum[st]);
    }

    bw.write(String.valueOf(minCost));

    br.close();
    bw.close();
  }
}
