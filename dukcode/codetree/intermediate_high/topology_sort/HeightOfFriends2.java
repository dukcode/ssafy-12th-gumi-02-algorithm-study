import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class HeightOfFriends2 {

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
    for (int i = 0; i < m; ++i) {
      st = new StringTokenizer(br.readLine());
      int a = Integer.parseInt(st.nextToken()) - 1;
      int b = Integer.parseInt(st.nextToken()) - 1;

      adj[a].add(b);
      inDegrees[b]++;
    }

    bw.write(solve() ? "Consistent" : "Inconsistent");

    br.close();
    bw.close();
  }

  private static boolean solve() {
    Queue<Integer> q = new ArrayDeque<>();
    for (int i = 0; i < n; i++) {
      if (inDegrees[i] == 0) {
        q.offer(i);
      }
    }

    List<Integer> order = new ArrayList<>();
    while (!q.isEmpty()) {
      order.add(q.peek());
      int here = q.poll();
      for (int there : adj[here]) {
        inDegrees[there]--;
        if (inDegrees[there] == 0) {
          q.offer(there);
        }
      }
    }

    if (order.size() != n) {
      return false;
    }

    for (int i = 0; i < n; i++) {
      if (inDegrees[i] != 0) {
        return false;
      }
    }

    return true;
  }

}
