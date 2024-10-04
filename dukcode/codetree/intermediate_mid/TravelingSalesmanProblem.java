import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class TravelingSalesmanProblem {

  private static final int MX = 987_654_321;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int[][] dist;

  private static boolean[] vis;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    n = Integer.parseInt(br.readLine());
    dist = new int[n][n];
    for (int y = 0; y < n; y++) {
      st = new StringTokenizer(br.readLine());
      for (int x = 0; x < n; x++) {
        dist[y][x] = Integer.parseInt(st.nextToken());
      }
    }

    vis = new boolean[n];
    vis[0] = true;
    bw.write(String.valueOf(solve(0, 0, 1)));

    br.close();
    bw.close();

  }

  private static int solve(int here, int sumDist, int cnt) {
    if (cnt == n) {
      return sumDist + (dist[here][0] == 0 ? MX : dist[here][0]);
    }

    int ret = MX;
    for (int there = 0; there < n; there++) {
      if (vis[there] || dist[here][there] == 0) {
        continue;
      }

      vis[there] = true;
      ret = Math.min(ret, solve(there, sumDist + dist[here][there], cnt + 1));
      vis[there] = false;
    }

    return ret;
  }

}
