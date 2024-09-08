import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class TreeFiveMoo {

  private static final long MX_LEN = 2_000_000_000L;

  private static BufferedReader br;
  private static BufferedWriter bw;

  private static int n;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));
    n = Integer.parseInt(br.readLine());

    bw.write(String.valueOf(solve()));

    br.close();
    bw.close();

  }

  private static long solve() {
    long minLen = 1;
    long maxLen = MX_LEN;

    while (minLen <= maxLen) {
      long halfLen = (minLen + maxLen) / 2;

      long halfNum = getLastNum(halfLen);

      if (halfNum < n) {
        minLen = halfLen + 1;
      } else {
        maxLen = halfLen - 1;
      }
    }

    return minLen;
  }

  private static long getLastNum(long len) {
    long numMoo = len / 3 + len / 5 - len / 15;
    return len - numMoo;
  }

}
