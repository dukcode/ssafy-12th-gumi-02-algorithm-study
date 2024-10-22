import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class B1027 {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static long[] arr;
  private static int[] cnt;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    n = Integer.parseInt(br.readLine());

    arr = new long[n];
    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < n; i++) {
      arr[i] = Long.parseLong(st.nextToken());
    }

    cnt = new int[n];
    for (int a = 0; a < n; a++) {
      for (int b = a + 1; b < n; b++) {
        if (canSee(a, b)) {
          cnt[a]++;
          cnt[b]++;
        }
      }
    }

    bw.write(String.valueOf(Arrays.stream(cnt).max().getAsInt()));

    br.close();
    bw.close();
  }

  private static boolean canSee(long a, long b) {
    for (long i = 1; i < b - a; ++i) {
      if (arr[(int) (a + i)] * (b - a) >=
          (b - a) * arr[(int) a] + i * (arr[(int) b] - arr[(int) a])) {
        return false;
      }
    }

    return true;
  }


}
