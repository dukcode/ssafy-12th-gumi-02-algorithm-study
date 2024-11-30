import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class GeologicalResearch {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int m;

  private static List<Integer>[] adj;
  private static int[] inDegrees;
  private static int[] maxPressures;
  private static int[] counts;

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
      int fr = Integer.parseInt(st.nextToken()) - 1;
      int to = Integer.parseInt(st.nextToken()) - 1;

      adj[fr].add(to);
      inDegrees[to]++;
    }

    maxPressures = new int[n];
    counts = new int[n];
    Queue<Integer> q = new LinkedList<>();
    for (int i = 0; i < n; i++) {
      if (inDegrees[i] == 0) {
        q.offer(i);
        maxPressures[i] = 1;
        counts[i]++;
      }
    }

    int ans = -1;
    while (!q.isEmpty()) {
      int here = q.poll();
      maxPressures[here] += counts[here] > 1 ? 1 : 0;
      ans = Math.max(ans, maxPressures[here]);
      for (int there : adj[here]) {
        if (maxPressures[there] < maxPressures[here]) {
          maxPressures[there] = maxPressures[here];
          counts[there] = 1;
        } else if (maxPressures[there] == maxPressures[here]) {
          counts[there]++;
        }

        inDegrees[there]--;
        if (inDegrees[there] == 0) {
          q.offer(there);
        }
      }
    }

    bw.write(String.valueOf(ans));

    br.close();
    bw.close();
  }


}
