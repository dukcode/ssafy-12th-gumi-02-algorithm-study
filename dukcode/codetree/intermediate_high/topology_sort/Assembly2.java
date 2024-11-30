import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Assembly2 {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int m;
  private static List<Integer>[] adj;
  private static int[] inDegrees;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());

    adj = new List[n];
    for (int i = 0; i < n; i++) {
      adj[i] = new ArrayList<>();
    }

    inDegrees = new int[n];
    for (int i = 0; i < m; i++) {
      st = new StringTokenizer(br.readLine());
      int to = Integer.parseInt(st.nextToken()) - 1;
      int k = Integer.parseInt(st.nextToken());

      st = new StringTokenizer(br.readLine());
      for (int idx = 0; idx < k; ++idx) {
        int from = Integer.parseInt(st.nextToken()) - 1;
        adj[from].add(to);
        inDegrees[to]++;
      }
    }

    Queue<Integer> q = new ArrayDeque<>();
    List<Integer> blocks = new ArrayList<>();

    int numItems = Integer.parseInt(br.readLine());
    boolean[] vis = new boolean[n];
    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < numItems; i++) {
      int item = Integer.parseInt(st.nextToken()) - 1;
      q.offer(item);
      vis[item] = true;
    }

    while (!q.isEmpty()) {
      int here = q.poll();
      blocks.add(here);
      for (int there : adj[here]) {
        inDegrees[there]--;
        if (vis[there] || inDegrees[there] != 0) {
          continue;
        }

        q.offer(there);
        vis[there] = true;
      }
    }

    Collections.sort(blocks);

    bw.write(String.valueOf(blocks.size()));
    bw.newLine();
    for (int block : blocks) {
      bw.write(String.valueOf(block + 1));
      bw.write(' ');
    }

    br.close();
    bw.close();
  }


}
