import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class CTags {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int m;

  private static String[] group1;
  private static String[] group2;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());

    group1 = new String[n];
    for (int i = 0; i < n; i++) {
      group1[i] = br.readLine();
    }

    group2 = new String[n];
    for (int i = 0; i < n; i++) {
      group2[i] = br.readLine();
    }

    int ans = 0;
    for (int i = 0; i < m; i++) {
      for (int j = i + 1; j < m; j++) {
        for (int k = j + 1; k < m; k++) {
          if (isOk(i, j, k)) {
            ans++;
          }
        }
      }
    }

    bw.write(String.valueOf(ans));

    br.close();
    bw.close();
  }

  private static boolean isOk(int i, int j, int k) {
    Set<String> set = new HashSet<>();
    for (int idx = 0; idx < n; ++idx) {
      set.add(toWord(group1[idx], i, j, k));
    }

    for (int idx = 0; idx < n; ++idx) {
      if (set.contains(toWord(group2[idx], i, j, k))) {
        return false;
      }
    }

    return true;
  }

  private static String toWord(String word, int i, int j, int k) {
    return String.valueOf(word.charAt(i))
        + word.charAt(j)
        + word.charAt(k);
  }

}
