import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class NPermutationsOfKWithRepetitionUnderConstraint {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int k;
  private static int n;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    k = Integer.parseInt(st.nextToken());
    n = Integer.parseInt(st.nextToken());

    List<Integer> picked = new ArrayList<>();
    solve(picked, 0);

    br.close();
    bw.close();

  }

  private static void solve(List<Integer> picked, int duplicated) throws IOException {
    if (picked.size() == n) {
      for (int num : picked) {
        bw.write(String.valueOf(num));
        bw.write(' ');
      }
      bw.newLine();
      return;
    }

    for (int i = 1; i <= k; ++i) {
      int nextDuplicated =
          (!picked.isEmpty() && picked.get(picked.size() - 1) == i ? duplicated : 0) + 1;

      if (nextDuplicated == 3) {
        continue;
      }

      picked.add(i);
      solve(picked, nextDuplicated);
      picked.remove(picked.size() - 1);
    }
  }

}
