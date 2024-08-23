import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Jlis {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int m;

  private static int[] arr1;
  private static int[] arr2;

  private static int[][] cache;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    int c = Integer.parseInt(br.readLine());
    while (c-- > 0) {
      st = new StringTokenizer(br.readLine());
      n = Integer.parseInt(st.nextToken());
      m = Integer.parseInt(st.nextToken());

      arr1 = new int[n];
      st = new StringTokenizer(br.readLine());
      for (int i = 0; i < n; i++) {
        arr1[i] = Integer.parseInt(st.nextToken());
      }

      arr2 = new int[m];
      st = new StringTokenizer(br.readLine());
      for (int i = 0; i < m; i++) {
        arr2[i] = Integer.parseInt(st.nextToken());
      }

      cache = new int[n + 1][m + 1];
      for (int y = 0; y <= n; ++y) {
        Arrays.fill(cache[y], -1);
      }

      bw.write(String.valueOf(jlis()));
      bw.newLine();
    }

    br.close();
    bw.close();
  }

  private static int jlis() {
    return jlis(-1, -1) - 2;
  }

  private static int jlis(int idx1, int idx2) {
    if (cache[idx1 + 1][idx2 + 1] != -1) {
      return cache[idx1 + 1][idx2 + 1];
    }

    long a = idx1 == -1 ? Long.MIN_VALUE : arr1[idx1];
    long b = idx2 == -1 ? Long.MIN_VALUE : arr2[idx2];

    long maxVal = Math.max(a, b);

    int ret = 2;

    for (int next = idx1 + 1; next < n; next++) {
      if (maxVal < arr1[next]) {
        ret = Math.max(ret, jlis(next, idx2) + 1);
      }
    }

    for (int next = idx2 + 1; next < m; next++) {
      if (maxVal < arr2[next]) {
        ret = Math.max(ret, jlis(idx1, next) + 1);
      }
    }

    return cache[idx1 + 1][idx2 + 1] = ret;
  }


}
