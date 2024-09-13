import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class DropTheBomb {

  private static final int MX_R = 1_000_000_000 / 2;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int k;
  private static int[] points;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    k = Integer.parseInt(st.nextToken());

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
    int minR = 0;
    int maxR = MX_R;

    while (minR <= maxR) {
      int halfR = (maxR + minR) / 2;
      if (cntBombs(halfR) > k) {
        minR = halfR + 1;
      } else {
        maxR = halfR - 1;
      }
    }
    return minR;
  }

  private static int cntBombs(int r) {
    int pos = points[0] + r;
    int ret = 1;
    for (int p : points) {
      if (pos - r <= p && p <= pos + r) {
        continue;
      }

      pos = p + r;
      ret += 1;
    }

    return ret;
  }


}
