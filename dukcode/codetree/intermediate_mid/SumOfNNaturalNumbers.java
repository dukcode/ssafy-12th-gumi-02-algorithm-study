import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class SumOfNNaturalNumbers {

  private static final long MX = 2_000_000_000;

  private static BufferedReader br;
  private static BufferedWriter bw;

  private static long s;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    s = Long.parseLong(br.readLine());
    bw.write(String.valueOf(solve()));

    br.close();
    bw.close();
  }

  private static long solve() {
    long l = 1;
    long r = MX;

    while (l <= r) {
      long half = (l + r) / 2;
      long sum = sumTo(half);
      if (sum <= s) {
        l = half + 1;
      } else {
        r = half - 1;
      }
    }

    return l - 1;
  }

  private static long sumTo(long b) {
    return b * (1 + b) / 2;
  }

}
