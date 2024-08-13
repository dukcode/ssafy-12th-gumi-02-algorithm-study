public class B1238 {

  private static final int MX = 987_654_321;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int m;
  private static int x;

  private static int[][] adj;
  private static int[][] times;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    input();
    init();
    int ans = solve();
    output(ans);

    br.close();
    bw.close();
  }

  private static void output(int ans) throws IOException {
    bw.write(String.valueOf(ans));
  }

  private static int solve() {
    for (int start = 0; start < n; start++) {
      dijkstra(start);
    }

    return max(times);
  }


  private static void dijkstra(int start) {
    // time, v
    PriorityQueue<Entry<Integer, Integer>> pq = new PriorityQueue<>(
        (a, b) -> a.getKey() == b.getKey() ?
            a.getValue() - b.getValue() :
            a.getKey() - b.getKey());

    pq.offer(new SimpleEntry<>(0, start));
    times[start][start] = 0;

    while (!pq.isEmpty()) {
      Entry<Integer, Integer> cur = pq.poll();
      int here = cur.getValue();
      int timeNow = cur.getKey();

      if (times[start][here] > timeNow) {
        continue;
      }

      for (int there = 0; there < n; ++there) {
        if (adj[here][there] == 0) {
          continue;
        }

        int timeThere = adj[here][there] + timeNow;

        if (timeThere >= times[start][there]) {
          continue;
        }

        pq.offer(new SimpleEntry<>(timeThere, there));
        times[start][there] = timeThere;
      }
    }
  }

  private static int max(int[][] times) {
    int ret = Integer.MIN_VALUE;

    for (int en = 0; en < n; ++en) {
      ret = Math.max(ret, times[x][en] + times[en][x]);
    }

    return ret;
  }

  private static void init() {
    times = new int[n][n];
    for (int i = 0; i < n; ++i) {
      Arrays.fill(times[i], MX);
    }
  }

  private static void input() throws IOException {
    st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());
    x = Integer.parseInt(st.nextToken()) - 1;

    adj = new int[n][n];

    for (int i = 0; i < m; ++i) {
      st = new StringTokenizer(br.readLine());
      int fr = Integer.parseInt(st.nextToken()) - 1;
      int to = Integer.parseInt(st.nextToken()) - 1;
      int t = Integer.parseInt(st.nextToken());
      adj[fr][to] = t;
    }
  }


}
