import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.Stack;
import java.util.StringTokenizer;

public class B6543 {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int m;

  private static boolean[][] adj;

  private static int[] discovered;
  private static int discoverCounter;

  private static int[] sccId;
  private static int sccCounter;
  private static Stack<Integer> sccStack;

  private static boolean[] isSccSink;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    while (input()) {
      tarjanScc();

      isSccSink = new boolean[sccCounter];
      Arrays.fill(isSccSink, true);

      for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
          if (!adj[i][j]) {
            continue;
          }

          if (sccId[i] != sccId[j]) {
            isSccSink[sccId[i]] = false;
            break;
          }
        }
      }

      for (int i = 0; i < n; ++i) {
        if (isSccSink[sccId[i]]) {
          bw.write(String.valueOf(i + 1));
          bw.write(' ');
        }
      }

      bw.newLine();
    }

    br.close();
    bw.close();
  }

  private static boolean input() throws IOException {
    st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());

    if (n == 0) {
      return false;
    }

    m = Integer.parseInt(st.nextToken());

    adj = new boolean[n][n];
    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < m; ++i) {
      int fr = Integer.parseInt(st.nextToken()) - 1;
      int to = Integer.parseInt(st.nextToken()) - 1;

      adj[fr][to] = true;
    }

    return true;
  }

  private static void tarjanScc() {
    sccId = new int[n];
    discovered = new int[n];

    Arrays.fill(sccId, -1);
    Arrays.fill(discovered, -1);

    discoverCounter = 0;

    sccCounter = 0;
    sccStack = new Stack<>();

    for (int i = 0; i < n; ++i) {
      if (discovered[i] == -1) {
        scc(i);
      }
    }
  }

  private static int scc(int here) {
    discovered[here] = discoverCounter++;
    sccStack.push(here);
    int ret = discovered[here];
    for (int there = 0; there < n; ++there) {
      if (!adj[here][there]) {
        continue;
      }

      if (discovered[there] == -1) {
        ret = Math.min(ret, scc(there));
      } else if (sccId[there] == -1) {
        ret = Math.min(ret, discovered[there]);
      }
    }

    if (ret == discovered[here]) {
      while (true) {
        int idx = sccStack.pop();
        sccId[idx] = sccCounter;
        if (idx == here) {
          break;
        }
      }
      sccCounter++;
    }

    return ret;
  }


}
