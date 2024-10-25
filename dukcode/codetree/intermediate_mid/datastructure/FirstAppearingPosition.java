import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Map.Entry;
import java.util.StringTokenizer;
import java.util.TreeMap;

public class FirstAppearingPosition {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    int n = Integer.parseInt(br.readLine());

    TreeMap<Integer, Integer> firstAppearance = new TreeMap<>();
    st = new StringTokenizer(br.readLine());
    for (int idx = 1; idx <= n; idx++) {
      int num = Integer.parseInt(st.nextToken());
      if (!firstAppearance.containsKey(num)) {
        firstAppearance.put(num, idx);
      }
    }

    for (Entry<Integer, Integer> e : firstAppearance.entrySet()) {
      bw.write(e.getKey() + " " + e.getValue() + "\n");
    }

    br.close();
    bw.close();
  }


}
