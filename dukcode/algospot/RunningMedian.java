import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class RunningMedian {

  private static final int MOD = 20_090_711;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int a;
  private static int b;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    int c = Integer.parseInt(br.readLine());
    while (c-- > 0) {
      st = new StringTokenizer(br.readLine());
      n = Integer.parseInt(st.nextToken());
      a = Integer.parseInt(st.nextToken());
      b = Integer.parseInt(st.nextToken());

      Generator generator = new Generator(a, b);

      PriorityQueue<Integer> lowerQ = new PriorityQueue<>(Comparator.reverseOrder());
      PriorityQueue<Integer> upperQ = new PriorityQueue<>(Comparator.naturalOrder());
      int sum = 0;
      for (int i = 0; i < n; i++) {
        int num = generator.next();

        if (lowerQ.size() == upperQ.size()) {
          lowerQ.offer(num);
        } else {
          upperQ.offer(num);
        }

        if (!lowerQ.isEmpty() && !upperQ.isEmpty() &&
            lowerQ.peek() > upperQ.peek()) {
          int a = upperQ.poll();
          int b = lowerQ.poll();
          upperQ.offer(b);
          lowerQ.offer(a);
        }

        sum = (sum + lowerQ.peek()) % MOD;
      }

      bw.write(String.valueOf(sum));
      bw.newLine();

    }

    br.close();
    bw.close();

  }

  private static class Generator {

    private static final int MOD = 20_090_711;

    private int seed;
    private int a;
    private int b;

    public Generator(int a, int b) {
      this.seed = 1983;
      this.a = a;
      this.b = b;
    }

    public int next() {
      int ret = seed;
      seed = (int) (((long) seed * a + b) % MOD);
      return ret;
    }
  }
}
