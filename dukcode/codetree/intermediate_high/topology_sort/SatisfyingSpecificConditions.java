import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class SatisfyingSpecificConditions {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static List<Integer>[] adj;
  private static int[] inDegrees;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    n = Integer.parseInt(br.readLine());

    adj = new List[n];
    for (int i = 0; i < n; i++) {
      adj[i] = new ArrayList<>();
    }
    inDegrees = new int[n];

    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < n - 1; i++) {
      String op = st.nextToken();

      if (op.equals("<")) {
        adj[i].add(i + 1);
        inDegrees[i + 1]++;
      } else {
        adj[i + 1].add(i);
        inDegrees[i]++;
      }
    }

    int[] ans1 = getResult(Comparator.naturalOrder());
    int[] ans2 = getResult(Comparator.reverseOrder());

    for (int num : ans1) {
      bw.write(String.format("%03d", num));
    }
    bw.newLine();

    for (int num : ans2) {
      bw.write(String.format("%03d", num));
    }
    bw.newLine();

    br.close();
    bw.close();
  }

  private static int[] getResult(Comparator<Integer> cmp) {
    PriorityQueue<Integer> pq = new PriorityQueue<>(cmp);
    int[] inDegree = new int[n];
    System.arraycopy(inDegrees, 0, inDegree, 0, n);
    for (int i = 0; i < n; i++) {
      if (inDegree[i] == 0) {
        pq.offer(i);
      }
    }

    List<Integer> order = new ArrayList<>();
    while (!pq.isEmpty()) {
      int here = pq.poll();
      order.add(here);
      for (int there : adj[here]) {
        inDegree[there]--;
        if (inDegree[there] == 0) {
          pq.offer(there);
        }
      }
    }

    int[] ret = new int[n];
    for (int i = 0; i < n; i++) {
      ret[order.get(i)] = i + 1;
    }

    return ret;
  }


}
