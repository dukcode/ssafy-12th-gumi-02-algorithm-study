import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class NumberOfUniqueBst {

  private static BufferedReader br;
  private static BufferedWriter bw;

  private static int n;

  private static int[] cache;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    n = Integer.parseInt(br.readLine());
    bw.write(String.valueOf(solve()));

    br.close();
    bw.close();

  }

  private static int solve() {
    cache = new int[n + 1];
    return solve(n);
  }

  private static int solve(int n) {
    if (n <= 1) {
      return 1;
    }

    if (cache[n] != 0) {
      return cache[n];
    }

    int ret = 0;
    for (int head = 1; head <= n; ++head) {
      int left = solve(head - 1);
      int right = solve(n - head);
      ret += left * right;
    }

    return cache[n] = ret;
  }

}
