import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class HashsetBasic {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    int n = Integer.parseInt(br.readLine());

    Set<Integer> set = new HashSet<>();
    for (int i = 0; i < n; i++) {
      st = new StringTokenizer(br.readLine());
      String command = st.nextToken();

      int value = Integer.parseInt(st.nextToken());
      switch (command) {
        case "add":
          set.add(value);
          break;
        case "remove":
          set.remove(value);
          break;
        case "find":
          bw.write(set.contains(value) ? "true" : "false");
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
