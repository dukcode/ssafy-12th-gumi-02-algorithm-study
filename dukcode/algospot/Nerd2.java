import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;
import java.util.TreeMap;

public class Nerd2 {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;

  private static TreeMap<Integer, Integer> tree;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));
    
    int c = Integer.parseInt(br.readLine());
    while (c-- > 0) {
      n = Integer.parseInt(br.readLine());

      tree = new TreeMap<>();
      int ans = 0;
      for (int i = 0; i < n; ++i) {
        st = new StringTokenizer(br.readLine());
        int p = Integer.parseInt(st.nextToken());
        int q = Integer.parseInt(st.nextToken());

        if (isDominated(p, q)) {
          ans += tree.size();
          continue;
        }

        removeDominated(p, q);
        tree.put(p, q);
        ans += tree.size();
      }

      bw.write(String.valueOf(ans));
      bw.newLine();

    }

    br.close();
    bw.close();
  }

  private static void removeDominated(int p, int q) {
    Integer floorKey = tree.floorKey(p);
    if (floorKey == null) {
      return;
    }

    while (floorKey != null) {
      if (tree.get(floorKey) > q) {
        break;
      }

      tree.remove(floorKey);
      floorKey = tree.floorKey(p);
    }
  }

  private static boolean isDominated(int p, int q) {
    Integer ceilingKey = tree.ceilingKey(p);

    if (ceilingKey == null) {
      return false;
    }

    return tree.get(ceilingKey) > q;
  }

}
