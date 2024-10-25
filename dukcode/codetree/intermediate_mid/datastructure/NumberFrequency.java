import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashMap;
import java.util.Map;
import java.util.StringJoiner;
import java.util.StringTokenizer;

public class NumberFrequency {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int m;

  private static Map<Integer, Integer> map;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());

    map = new HashMap<>();
    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < n; i++) {
      int num = Integer.parseInt(st.nextToken());
      map.put(num, map.getOrDefault(num, 0) + 1);
    }

    StringJoiner sj = new StringJoiner(" ");
    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < m; ++i) {
      int target = Integer.parseInt(st.nextToken());
      sj.add(String.valueOf(map.getOrDefault(target, 0)));
    }

    bw.write(sj.toString());

    br.close();
    bw.close();
  }

}
