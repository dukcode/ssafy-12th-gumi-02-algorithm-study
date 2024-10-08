import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

// 요리사
public class S4012 {

  private static final int MX = 987_654_321;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int t;

  private static int n;
  private static int[][] s;

  private static boolean[] taken;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    t = Integer.parseInt(br.readLine());
    for (int tc = 1; tc <= t; tc++) {
      n = Integer.parseInt(br.readLine());

      s = new int[n][n];
      for (int y = 0; y < n; ++y) {
        st = new StringTokenizer(br.readLine());
        for (int x = 0; x < n; ++x) {
          s[y][x] = Integer.parseInt(st.nextToken());
        }
      }

      taken = new boolean[n];

      bw.write("#" + tc + " ");
      bw.write(String.valueOf(solve(-1, 0)));
      bw.newLine();
    }

    br.close();
    bw.close();
  }

  private static int solve(int lastIdx, int cnt) {
    if (cnt == n / 2) {
      return calcScore();
    }

    int ret = MX;
    for (int nextIdx = lastIdx + 1; nextIdx < n; ++nextIdx) {
      taken[nextIdx] = true;
      ret = Math.min(ret, solve(nextIdx, cnt + 1));
      taken[nextIdx] = false;
    }

    return ret;
  }

  private static int calcScore() {
    int score1 = 0;
    int score2 = 0;

    for (int i = 0; i < n; ++i) {
      for (int j = i + 1; j < n; ++j) {
        if (taken[i] && taken[j]) {
          score1 += s[i][j] + s[j][i];
        }

        if (!taken[i] && !taken[j]) {
          score2 += s[i][j] + s[j][i];
        }
      }
    }

    return Math.abs(score1 - score2);
  }


}
