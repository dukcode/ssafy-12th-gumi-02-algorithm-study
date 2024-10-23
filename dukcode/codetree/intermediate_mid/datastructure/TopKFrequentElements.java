import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Objects;
import java.util.StringJoiner;
import java.util.StringTokenizer;

public class TopKFrequentElements {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int k;

  private static Map<Integer, Integer> freq;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    k = Integer.parseInt(st.nextToken());

    freq = new HashMap<>();
    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < n; i++) {
      int num = Integer.parseInt(st.nextToken());
      freq.put(num, freq.getOrDefault(num, 0) + 1);
    }

    List<Entry<Integer, Integer>> keyValues = new ArrayList<>(freq.entrySet());
    keyValues.sort(
        (e1, e2) -> Objects.equals(e1.getValue(), e2.getValue()) ?
            Integer.compare(e2.getKey(), e1.getKey()) :
            Integer.compare(e2.getValue(), e1.getValue()));

    StringJoiner sj = new StringJoiner(" ");
    for (int i = 0; i < k; i++) {
      sj.add(String.valueOf(keyValues.get(i).getKey()));
    }

    bw.write(sj.toString());

    br.close();
    bw.close();
  }


}
