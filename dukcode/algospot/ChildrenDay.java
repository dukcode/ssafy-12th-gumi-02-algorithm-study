import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;

public class ChildrenDay {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static String d;
  private static int n;
  private static int m;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    int c = Integer.parseInt(br.readLine());
    while (c-- > 0) {
      st = new StringTokenizer(br.readLine());
      d = st.nextToken();
      n = Integer.parseInt(st.nextToken());
      m = Integer.parseInt(st.nextToken());

      bw.write(gifts(d, n, m));
      bw.newLine();
    }

    br.close();
    bw.close();
  }

  private static int append(int here, int edge, int mod) {
    int there = here * 10 + edge;
    if (there >= mod) {
      return mod + there % mod;
    }

    return there % mod;
  }

  private static String gifts(String digits, int n, int m) {
    digits = sort(digits);

    int[] parent = new int[2 * n];
    Arrays.fill(parent, -1);
    int[] choice = new int[2 * n];
    Arrays.fill(choice, -1);

    Queue<Integer> q = new ArrayDeque<>();
    parent[0] = 0;
    q.offer(0);
    while (!q.isEmpty()) {
      int here = q.poll();
      for (char ch : digits.toCharArray()) {
        int i = ch - '0';
        int there = append(here, i, n);
        if (parent[there] != -1) {
          continue;
        }

        parent[there] = here;
        choice[there] = i;
        q.offer(there);
      }
    }

    if (parent[n + m] == -1) {
      return "IMPOSSIBLE";
    }

    StringBuilder sb = new StringBuilder();
    int here = n + m;
    while (parent[here] != here) {
      sb.append((char) (choice[here] + '0'));
      here = parent[here];
    }

    sb.reverse();
    return sb.toString();
  }

  private static String sort(String str) {
    char[] chArr = str.toCharArray();
    Arrays.sort(chArr);
    return String.valueOf(chArr);
  }

}
