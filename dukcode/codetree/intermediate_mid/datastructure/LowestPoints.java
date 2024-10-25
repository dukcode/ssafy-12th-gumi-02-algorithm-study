import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class LowestPoints {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    n = Integer.parseInt(br.readLine());

    Map<Long, Long> map = new HashMap<>();
    for (int i = 0; i < n; i++) {
      st = new StringTokenizer(br.readLine());
      long x = Long.parseLong(st.nextToken());
      long y = Long.parseLong(st.nextToken());

      if (map.containsKey(x)) {
        map.put(x, Math.min(y, map.get(x)));
        continue;
      }

      map.put(x, y);
    }

    long ans = map.values().stream().reduce(0L, Long::sum);
    bw.write(String.valueOf(ans));

    br.close();
    bw.close();
  }


}
