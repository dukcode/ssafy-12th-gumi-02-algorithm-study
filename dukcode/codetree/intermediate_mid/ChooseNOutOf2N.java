import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class ChooseNOutOf2N {

  private static final int MX = 987_654_321;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int[] arr;

  private static int sumAll;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    n = Integer.parseInt(br.readLine());

    sumAll = 0;
    arr = new int[2 * n];
    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < 2 * n; i++) {
      arr[i] = Integer.parseInt(st.nextToken());
      sumAll += arr[i];
    }

    bw.write(String.valueOf(solve(-1, 0, 0)));

    br.close();
    bw.close();

  }

  private static int solve(int lastIdx, int cnt, int sum) {
    if (cnt == n) {
      return Math.abs(sumAll - sum - sum);
    }

    int ret = MX;
    for (int nextIdx = lastIdx + 1; nextIdx < 2 * n; nextIdx++) {
      ret = Math.min(ret, solve(nextIdx, cnt + 1, sum + arr[nextIdx]));
    }

    return ret;
  }

}
