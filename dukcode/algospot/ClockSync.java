import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class ClockSync {

  private static final int MX = 987_654_321;

  private static final int NUM_SWITCHES = 10;
  private static final int NUM_CLOCKS = 16;

  private static final int[][] SWITCHES = {
      {0, 1, 2},
      {3, 7, 9, 11},
      {4, 10, 14, 15},
      {0, 4, 5, 6, 7},
      {6, 7, 8, 10, 12},
      {0, 2, 14, 15},
      {3, 14, 15},
      {4, 5, 7, 14, 15},
      {1, 2, 3, 4, 5},
      {3, 4, 5, 9, 13},
  };

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int[] clocks;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    int c = Integer.parseInt(br.readLine());
    while (c-- > 0) {

      clocks = new int[NUM_CLOCKS];
      st = new StringTokenizer(br.readLine());
      for (int i = 0; i < NUM_CLOCKS; i++) {
        clocks[i] = Integer.parseInt(st.nextToken()) % 12;
      }

      int ans = countClick(0, 0);
      bw.write(String.valueOf(ans == MX ? -1 : ans));
      bw.newLine();
    }

    br.close();
    bw.close();

  }

  private static int countClick(int idxSw, int numClicked) {
    if (idxSw == NUM_SWITCHES) {
      return isAligned() ? numClicked : MX;
    }

    int ret = MX;
    for (int numClick = 0; numClick < 4; ++numClick) {
      ret = Math.min(ret, countClick(idxSw + 1, numClicked + numClick));
      click(idxSw);
    }

    return ret;
  }

  private static void click(int idxSw) {
    for (int target : SWITCHES[idxSw]) {
      clocks[target] = (clocks[target] + 3) % 12;
    }
  }

  private static boolean isAligned() {
    for (int i = 0; i < NUM_CLOCKS; i++) {
      if (clocks[i] != 0) {
        return false;
      }
    }

    return true;
  }
}
