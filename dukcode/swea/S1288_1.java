import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

/**
 * 새로운 불면증 치료법
 */
public class S1288_1 {

  private static final int END = (1 << 10) - 1;

  private static BufferedReader br;
  private static BufferedWriter bw;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    int t = Integer.parseInt(br.readLine());
    for (int tc = 1; tc <= t; tc++) {
      int n = Integer.parseInt(br.readLine());
      bw.write(String.format("#%d %d\n", tc, solve(n)));
    }

    br.close();
    bw.close();
  }

  private static int solve(int base) {
    int appeared = 0;

    int num = base;
    int cnt = 0;
    do {
      cnt++;
      appeared = checkAppeared(appeared, num);
      num += base;
    } while (appeared != END);

    return cnt * base;
  }

  private static int checkAppeared(int appeared, int num) {
    while (num > 0) {
      appeared = appeared | 1 << (num % 10);
      num /= 10;
    }

    return appeared;
  }

}
