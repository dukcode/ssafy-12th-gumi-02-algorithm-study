import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;
import java.util.stream.IntStream;

public class ChangingSeats2 {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int k;

  private static int[] a;
  private static int[] b;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    k = Integer.parseInt(st.nextToken());

    int[] seat = IntStream.rangeClosed(0, n - 1).toArray();
    Set<Integer>[] record = new Set[n];
    for (int i = 0; i < n; i++) {
      record[i] = new HashSet<>();
      record[i].add(i);
    }

    a = new int[k];
    b = new int[k];
    for (int i = 0; i < k; i++) {
      st = new StringTokenizer(br.readLine());
      a[i] = Integer.parseInt(st.nextToken()) - 1;
      b[i] = Integer.parseInt(st.nextToken()) - 1;
    }

    for (int i = 0; i < 3 * k; i++) {
      record[seat[a[i % k]]].add(b[i % k]);
      record[seat[b[i % k]]].add(a[i % k]);

      int tmp = seat[a[i % k]];
      seat[a[i % k]] = seat[b[i % k]];
      seat[b[i % k]] = tmp;
    }

    for (int i = 0; i < n; i++) {
      bw.write(String.valueOf(record[i].size()));
      bw.newLine();
    }

    br.close();
    bw.close();
  }


}
