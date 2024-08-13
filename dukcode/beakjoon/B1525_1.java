import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayDeque;
import java.util.HashMap;
import java.util.Map;
import java.util.Queue;
import java.util.StringTokenizer;

public class B1525_1 {

  private static final int[] dy = {-1, 0, 0, 1};
  private static final int[] dx = {0, -1, 1, 0};

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;
  private static StringBuilder sb;

  private static String start;
  private static String end;

  private static int n = 3;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    sb = new StringBuilder();
    for (int y = 0; y < n; y++) {
      st = new StringTokenizer(br.readLine());
      for (int x = 0; x < n; x++) {
        sb.append(st.nextToken());
      }
    }

    start = sb.toString();

    sb = new StringBuilder();
    for (int i = 1; i < n * n; i++) {
      sb.append(i);
    }
    sb.append(0);

    end = sb.toString();

    bw.write(String.valueOf(solve()));

    br.close();
    bw.close();

  }

  private static int solve() {
    if (start.equals(end)) {
      return 0;
    }
    Map<String, Integer> dist = new HashMap<>();
    Queue<String> q = new ArrayDeque<>();

    q.offer(start);
    dist.put(start, 1);
    q.offer(end);
    dist.put(end, -1);

    while (!q.isEmpty()) {
      String cur = q.poll();
      int curDist = dist.get(cur);

      int pos = cur.indexOf('0');
      int y = pos / n;
      int x = pos % n;
      for (int dir = 0; dir < 4; ++dir) {
        int ny = y + dy[dir];
        int nx = x + dx[dir];

        if (ny < 0 || ny >= n || nx < 0 || nx >= n) {
          continue;
        }

        String next = swap(cur, n * ny + nx);

        Integer d = dist.get(next);

        if (d == null) {
          q.offer(next);
          dist.put(next, increase(curDist));
          continue;
        }

        if (sign(d) != sign(curDist)) {
          return Math.abs(d) + Math.abs(curDist) - 1;
        }
      }
    }

    return -1;
  }

  private static int sign(int value) {
    if (value < 0) {
      return -1;
    }

    return 1;
  }

  private static int increase(int value) {
    if (value < 0) {
      return value - 1;
    }
    return value + 1;
  }

  private static String swap(String s, int j) {
    char toChange = s.charAt(j);
    return s.replace(toChange, 'A')
        .replace('0', toChange)
        .replace('A', '0');
  }

}

