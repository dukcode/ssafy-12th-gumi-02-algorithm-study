import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;
import java.util.Queue;

public class MakeOneUsingFourOperations {

  private static BufferedReader br;
  private static BufferedWriter bw;

  private static int n;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    n = Integer.parseInt(br.readLine());

    bw.write(String.valueOf(solve() - 1));

    br.close();
    bw.close();

  }

  private static int solve() {
    Queue<Integer> q = new LinkedList<>();
    Map<Integer, Integer> dist = new HashMap<>();

    q.offer(n);
    dist.put(n, 1);

    while (!q.isEmpty()) {
      int cur = q.poll();

      if (cur == 1) {
        return dist.get(cur);
      }

      if (!dist.containsKey(cur - 1)) {
        q.offer(cur - 1);
        dist.put(cur - 1, dist.get(cur) + 1);
      }

      if (!dist.containsKey(cur + 1)) {
        q.offer(cur + 1);
        dist.put(cur + 1, dist.get(cur) + 1);
      }

      if (cur % 2 == 0 && !dist.containsKey(cur / 2)) {
        q.offer(cur / 2);
        dist.put(cur / 2, dist.get(cur) + 1);
      }

      if (cur % 3 == 0 && !dist.containsKey(cur / 3)) {
        q.offer(cur / 3);
        dist.put(cur / 3, dist.get(cur) + 1);
      }
    }

    return 0;
  }

}
