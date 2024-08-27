import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class B11725 {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;

  private static List<Integer>[] adj;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    n = Integer.parseInt(br.readLine());

    adj = new List[n];
    for (int i = 0; i < n; i++) {
      adj[i] = new ArrayList<>();
    }

    for (int i = 0; i < n - 1; ++i) {
      st = new StringTokenizer(br.readLine());
      int first = Integer.parseInt(st.nextToken()) - 1;
      int second = Integer.parseInt(st.nextToken()) - 1;
      adj[first].add(second);
      adj[second].add(first);
    }

    int[] parent = new int[n];
    Arrays.fill(parent, -1);

    Queue<Integer> q = new ArrayDeque<>();
    q.offer(0);
    parent[0] = 0;

    while (!q.isEmpty()) {
      int cur = q.poll();
      for (int next : adj[cur]) {
        if (parent[next] != -1) {
          continue;
        }
        parent[next] = cur;
        q.offer(next);
      }
    }

    for (int i = 1; i < n; ++i) {
      bw.write(String.valueOf(parent[i] + 1));
      bw.newLine();
    }

    br.close();
    bw.close();
  }

}
