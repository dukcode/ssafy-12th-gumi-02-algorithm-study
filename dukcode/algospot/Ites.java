import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Ites {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int k;
  private static int n;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    int c = Integer.parseInt(br.readLine());
    while (c-- > 0) {
      st = new StringTokenizer(br.readLine());
      k = Integer.parseInt(st.nextToken());
      n = Integer.parseInt(st.nextToken());

      Queue<Integer> q = new ArrayDeque<>();
      int cnt = 0;
      int sum = 0;
      Generator gen = new Generator();
      for (int i = 0; i < n; ++i) {
        int num = gen.next();

        q.offer(num);
        sum += num;

        while (!q.isEmpty() && sum > k) {
          sum -= q.poll();
        }

        if (sum == k) {
          cnt++;
        }
      }

      bw.write(String.valueOf(cnt));
      bw.newLine();
    }

    br.close();
    bw.close();
  }

  private static class Generator {

    private long seed = 1983;

    private int next() {
      int ret = (int) (seed % 10000) + 1;
      seed = (seed * 214013 + 2531011) % (1L << 32);
      return ret;
    }
  }


}
