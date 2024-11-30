import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Assembly {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int m;

  private static int[][] adj;
  private static int[] inDegrees;
  private static int[][] numBlocks;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());

    adj = new int[n][n];
    inDegrees = new int[n];
    for (int i = 0; i < m; i++) {
      st = new StringTokenizer(br.readLine());
      int to = Integer.parseInt(st.nextToken()) - 1;
      int fr = Integer.parseInt(st.nextToken()) - 1;
      int num = Integer.parseInt(st.nextToken());

      adj[fr][to] = num;
      inDegrees[to]++;
    }

    numBlocks = new int[n][n];

    Queue<Integer> q = new LinkedList<>();
    for (int i = 0; i < n; i++) {
      if (inDegrees[i] == 0) {
        q.offer(i);
        numBlocks[i][i] = 1;
      }
    }

    while (!q.isEmpty()) {
      int here = q.poll();
      for (int there = 0; there < n; ++there) {
        if (adj[here][there] == 0) {
          continue;
        }
        for (int i = 0; i < n; ++i) {
          numBlocks[there][i] += numBlocks[here][i] * adj[here][there];
        }

        inDegrees[there]--;

        if (inDegrees[there] == 0) {
          q.offer(there);
        }
      }
    }

    for (int i = 0; i < n; i++) {
      if (numBlocks[n - 1][i] == 0) {
        continue;
      }

      bw.write(String.valueOf(i + 1));
      bw.write(' ');
      bw.write(String.valueOf(numBlocks[n - 1][i]));
      bw.newLine();
    }

    br.close();
    bw.close();
  }


}
