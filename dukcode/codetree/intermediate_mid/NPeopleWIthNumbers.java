import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class NPeopleWithNumbers {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int maxT;
  private static int[] times;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    input();
    int ans = solve();
    bw.write(String.valueOf(ans));

    br.close();
    bw.close();
  }

  private static int solve() {
    int minK = 1;
    int maxK = n;

    while (minK <= maxK) {
      int halfK = (minK + maxK) / 2;

      if (getTime(halfK) > maxT) {
        minK = halfK + 1;
      } else {
        maxK = halfK - 1;
      }

    }

    return minK;
  }

  private static int getTime(int k) {
    PriorityQueue<Integer> pq = new PriorityQueue<>();
    for (int i = 0; i < n; i++) {
      if (pq.size() < k) {
        pq.offer(times[i]);
        continue;
      }

      pq.offer(pq.poll() + times[i]);
    }

    int ret = 0;
    while (!pq.isEmpty()) {
      ret = pq.poll();
    }

    return ret;
  }

  private static void input() throws IOException {
    st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    maxT = Integer.parseInt(st.nextToken());

    times = new int[n];
    for (int i = 0; i < n; i++) {
      times[i] = Integer.parseInt(br.readLine());
    }
  }


}
