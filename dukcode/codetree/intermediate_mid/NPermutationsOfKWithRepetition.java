import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class NPermutationsOfKWithRepetition {

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

    List<Integer> arr = new ArrayList<>();
    solve(arr);

    br.close();
    bw.close();

  }

  private static void solve(List<Integer> arr) throws IOException {
    if (arr.size() == n) {
      for (Integer num : arr) {
        bw.write(String.valueOf(num));
        bw.write(' ');
      }
      bw.newLine();
      return;
    }

    for (int i = 1; i <= k; ++i) {
      arr.add(i);
      solve(arr);
      arr.remove(arr.size() - 1);
    }
  }
}
