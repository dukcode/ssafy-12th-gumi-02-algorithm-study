import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringJoiner;
import java.util.StringTokenizer;
import java.util.TreeMap;

public class TreemapBasic {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    TreeMap<Integer, Integer> tree = new TreeMap<>();
    int n = Integer.parseInt(br.readLine());
    for (int i = 0; i < n; i++) {
      st = new StringTokenizer(br.readLine());
      String command = st.nextToken();

      int key;
      int value;
      switch (command) {
        case "add":
          key = Integer.parseInt(st.nextToken());
          value = Integer.parseInt(st.nextToken());
          tree.put(key, value);
          break;
        case "remove":
          key = Integer.parseInt(st.nextToken());
          tree.remove(key);
          break;
        case "find":
          key = Integer.parseInt(st.nextToken());
          if (!tree.containsKey(key)) {
            bw.write("None");
            bw.newLine();
            break;
          }

          bw.write(String.valueOf(tree.get(key)));
          bw.newLine();
          break;
        case "print_list":
          if (tree.isEmpty()) {
            bw.write("None");
            bw.newLine();
            break;
          }

          StringJoiner sj = new StringJoiner(" ");
          for (int val : tree.values()) {
            sj.add(String.valueOf(val));
          }

          bw.write(sj.toString());
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
