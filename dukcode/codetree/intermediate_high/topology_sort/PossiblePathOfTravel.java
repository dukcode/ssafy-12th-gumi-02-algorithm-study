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

public class PossiblePathOfTravel {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int m;
  private static List<Integer>[] adj;
  private static int[] inDegrees;

  private static int[] numWays;

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

    numWays = new int[n];
    numWays[0] = 1;

    Queue<Integer> q = new LinkedList<>();
    for (int i = 0; i < n; i++) {
      if (inDegrees[i] == 0) {
        q.offer(i);
      }
    }

    while (!q.isEmpty()) {
      int here = q.poll();
      for (int there : adj[here]) {
        numWays[there] += numWays[here];

        inDegrees[there]--;
        if (inDegrees[there] == 0) {
          q.offer(there);
        }
      }
    }

    bw.write(String.valueOf(numWays[n - 1]));

    br.close();
    bw.close();
  }


}
