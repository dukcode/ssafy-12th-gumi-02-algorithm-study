import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class DistributingIntegers {

  private static final int MX = 100_000;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int m;
  private static int[] arr;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());

    arr = new int[n];
    for (int i = 0; i < n; ++i) {
      arr[i] = Integer.parseInt(br.readLine());
    }

    bw.write(String.valueOf(solve()));

    br.close();
    bw.close();

  }

  private static int solve() {
    int st = 1;
    int en = MX;

    while (st <= en) {
      int half = (st + en) / 2;

      if (numOfParts(arr, half) >= m) {
        st = half + 1;
      } else {
        en = half - 1;
      }
    }

    return st - 1;
  }

  private static int numOfParts(int[] arr, int div) {
    int ret = 0;
    for (int num : arr) {
      ret += num / div;
    }

    return ret;
  }

}
