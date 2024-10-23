import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class HashmapBasic {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    n = Integer.parseInt(br.readLine());

    Map<Integer, Integer> m = new HashMap<>();

    for (int i = 0; i < n; i++) {
      st = new StringTokenizer(br.readLine());

      String command = st.nextToken();

      int key;
      int value;

      switch (command) {
        case "add":
          key = Integer.parseInt(st.nextToken());
          value = Integer.parseInt(st.nextToken());
          m.put(key, value);
          break;
        case "remove":
          key = Integer.parseInt(st.nextToken());
          m.remove(key);
          break;
        case "find":
          key = Integer.parseInt(st.nextToken());
          if (!m.containsKey(key)) {
            bw.write("None");
            bw.newLine();
            break;
          }

          bw.write(String.valueOf(m.get(key)));
          bw.newLine();

          break;
        default:
          break;
      }
    }

    br.close();
    bw.close();
  }


}
