import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Snail {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int m;

  private static double[][] cache;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    int c = Integer.parseInt(br.readLine());
    while (c-- > 0) {
      st = new StringTokenizer(br.readLine());
      n = Integer.parseInt(st.nextToken()); // 거리
      m = Integer.parseInt(st.nextToken()); // 날짜

      bw.write(String.format("%.10f", solve()));
      bw.newLine();
    }

    br.close();
    bw.close();
  }

  private static double solve() {
    cache = new double[m][m * 2 + 1];
    for (int y = 0; y < m; ++y) {
      Arrays.fill(cache[y], -1.0);
    }

    return calcProb(m, 0);
  }

  private static double calcProb(int leftDays, int climbed) {
    if (leftDays == 0) {
      return climbed >= n ? 1.0 : 0.0;
    }

    if (cache[leftDays - 1][climbed] != -1) {
      return cache[leftDays - 1][climbed];
    }
    return cache[leftDays - 1][climbed] = 0.75 * calcProb(leftDays - 1, climbed + 2) +
        0.25 * calcProb(leftDays - 1, climbed + 1);
  }


}
