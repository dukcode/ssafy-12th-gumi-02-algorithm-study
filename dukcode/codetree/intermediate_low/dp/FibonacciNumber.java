import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class FibonacciNumber {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int[] cache;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    n = Integer.parseInt(br.readLine());

    cache = new int[n];
    bw.write(String.valueOf(fibonacci(n - 1)));

    br.close();
    bw.close();

  }

  private static int fibonacci(int idx) {
    if (idx <= 1) {
      return 1;
    }

    if (cache[idx] != 0) {
      return cache[idx];
    }

    return cache[idx] = fibonacci(idx - 1) + fibonacci(idx - 2);
  }

}
