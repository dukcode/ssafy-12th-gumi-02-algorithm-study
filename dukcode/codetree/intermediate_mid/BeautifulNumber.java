import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class BeautifulNumber {

  private static BufferedReader br;
  private static BufferedWriter bw;

  private static int n;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    n = Integer.parseInt(br.readLine());

    bw.write(String.valueOf(solve(0)));

    br.close();
    bw.close();

  }

  private static int solve(int cnt) {
    if (cnt == n) {
      return 1;
    }

    int ret = 0;
    for (int i = 1; i <= 4; ++i) {
      if (cnt + i > n) {
        continue;
      }

      ret += solve(cnt + i);
    }

    return ret;
  }

}
