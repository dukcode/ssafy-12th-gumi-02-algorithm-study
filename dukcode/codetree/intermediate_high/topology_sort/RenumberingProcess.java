import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class RenumberingProcess {

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
      int a = Integer.parseInt(st.nextToken()) - 1;
      int b = Integer.parseInt(st.nextToken()) - 1;

      adj[b].add(a);
      inDegrees[a]++;
    }

    PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> b - a);
    for (int i = 0; i < n; i++) {
      if (inDegrees[i] == 0) {
        pq.offer(i);
      }
    }

    int[] mappings = new int[n];
    int order = n;
    int visCnt = 0;

    while (!pq.isEmpty()) {
      int here = pq.poll();
      mappings[here] = order--;
      visCnt++;
      for (int there : adj[here]) {

        inDegrees[there]--;

        if (inDegrees[there] != 0) {
          continue;
        }

        pq.offer(there);
      }
    }

    if (visCnt != n) {
      bw.write("-1");
    } else {
      for (int mapping : mappings) {
        bw.write(String.valueOf(mapping));
        bw.write(' ');
      }
    }

    br.close();
    bw.close();
  }

}
