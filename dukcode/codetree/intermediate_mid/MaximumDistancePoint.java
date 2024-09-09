import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class MaximumDistancePoint {

  private static final int MX = 1_000_000_000;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int m;

  private static int[] points;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());

    points = new int[n];
    for (int i = 0; i < n; i++) {
      points[i] = Integer.parseInt(br.readLine());
    }

    Arrays.sort(points);

    bw.write(String.valueOf(solve()));

    br.close();
    bw.close();
  }

  private static int solve() {
    int minDist = 1;
    int maxDist = MX;

    while (minDist <= maxDist) {
      int halfDist = (maxDist + minDist) / 2;

      if (countProducts(halfDist) >= m) {
        minDist = halfDist + 1;
      } else {
        maxDist = halfDist - 1;
      }
    }

    return minDist - 1;
  }


  private static int countProducts(int minDist) {
    int cnt = 1;
    int lastPos = points[0];

    for (int i = 1; i < n; ++i) {
      if (points[i] - lastPos >= minDist) {
        cnt++;
        lastPos = points[i];
      }
    }

    return cnt;
  }


}
