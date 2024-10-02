import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class The1DBombGame {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int m;

  private static int[] bombs;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());

    bombs = new int[n];
    for (int i = 0; i < n; ++i) {
      bombs[i] = Integer.parseInt(br.readLine());
    }

    while (true) {
      if (!boom()) {
        break;
      }
    }

    bw.write(String.valueOf(bombs.length));
    bw.newLine();

    for (int bomb : bombs) {
      bw.write(String.valueOf(bomb));
      bw.newLine();
    }

    br.close();
    bw.close();
  }

  private static boolean boom() {
    boolean boomed = false;
    if (bombs.length == 0) {
      return false;
    }
    int pivot = bombs[0];
    int cnt = 0;
    for (int idx = 0; idx < bombs.length; ++idx) {
      if (pivot == bombs[idx]) {
        cnt++;
        continue;
      }

      if (boom(cnt, idx)) {
        boomed = true;
      }

      pivot = bombs[idx];
      cnt = 1;
    }

    if (boom(cnt, bombs.length)) {
      boomed = true;
    }

    drop();

    return boomed;
  }

  private static boolean boom(int cnt, int from) {
    if (cnt >= m) {
      for (int idx = from - 1; idx >= from - cnt; --idx) {
        bombs[idx] = 0;
      }
      return true;
    }

    return false;
  }

  private static void drop() {
    List<Integer> tmp = new ArrayList<>();
    for (int bomb : bombs) {
      if (bomb == 0) {
        continue;
      }

      tmp.add(bomb);
    }

    bombs = tmp.stream().mapToInt(Integer::intValue).toArray();
  }


}
