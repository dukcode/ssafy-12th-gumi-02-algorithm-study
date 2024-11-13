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

public class Predecessor {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;

  private static List<Integer>[] adj;
  private static int[] inDegrees;

  private static int[] times;

  private static int[] cumulativeTimes;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    n = Integer.parseInt(br.readLine());

    adj = new List[n];
    for (int i = 0; i < n; i++) {
      adj[i] = new ArrayList<>();
    }

    times = new int[n];
    cumulativeTimes = new int[n];
    inDegrees = new int[n];
    for (int idx = 0; idx < n; idx++) {
      st = new StringTokenizer(br.readLine());
      int time = Integer.parseInt(st.nextToken());
      times[idx] = time;
      cumulativeTimes[idx] = time;
      int numNeeds = Integer.parseInt(st.nextToken());

      for (int j = 0; j < numNeeds; j++) {
        int need = Integer.parseInt(st.nextToken()) - 1;
        adj[need].add(idx);
        inDegrees[idx]++;
      }
    }

    Queue<Integer> q = new LinkedList<>();
    for (int i = 0; i < n; i++) {
      if (inDegrees[i] == 0) {
        q.offer(i);
      }
    }

    int ans = -1;
    while (!q.isEmpty()) {
      int here = q.poll();
      for (int there : adj[here]) {
        cumulativeTimes[there] = Math.max(cumulativeTimes[there],
            cumulativeTimes[here] + times[there]);
        ans = Math.max(ans, cumulativeTimes[there]);
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
