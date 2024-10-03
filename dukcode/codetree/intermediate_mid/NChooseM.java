import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class NChooseM {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int m;

  private static List<Integer> arr;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());

    arr = new ArrayList<>();
    printCombination(0, 0);

    br.close();
    bw.close();

  }

  private static void printCombination(int last, int cnt) throws IOException {
    if (cnt == m) {
      printCombination();
      return;
    }

    for (int next = last + 1; next <= n; ++next) {
      arr.add(next);
      printCombination(next, cnt + 1);
      arr.remove(arr.size() - 1);
    }
  }

  private static void printCombination() throws IOException {
    for (Integer num : arr) {
      bw.write(String.valueOf(num));
      bw.write(' ');
    }
    bw.newLine();
  }


}
