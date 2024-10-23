import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;
import java.util.StringTokenizer;

public class SumOfTwoNum {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int k;

  private static Map<Integer, Integer> map;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    k = Integer.parseInt(st.nextToken());

    st = new StringTokenizer(br.readLine());
    map = new HashMap<>();
    for (int i = 0; i < n; i++) {
      int num = Integer.parseInt(st.nextToken());
      map.put(num, map.getOrDefault(num, 0) + 1);
    }

    Set<Integer> keys = map.keySet();
    int ans = 0;
    for (Integer key : keys) {
      int counter = k - key;

      if (key == counter) {
        ans += map.get(key) * (map.get(key) - 1);
        continue;
      }

      ans += map.get(key) * map.getOrDefault(counter, 0);
    }

    ans /= 2;
    bw.write(String.valueOf(ans));

    br.close();
    bw.close();
  }


}
