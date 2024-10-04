import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class BackwardPermutation {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static boolean[] taken;
  private static List<Integer> permutation;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    n = Integer.parseInt(br.readLine());

    taken = new boolean[n];
    permutation = new ArrayList<>();
    printPermutation(0);

    br.close();
    bw.close();

  }

  private static void printPermutation(int cnt) throws IOException {
    if (cnt == n) {
      print(permutation);
      return;
    }

    for (int num = n; num >= 1; --num) {
      if (taken[num - 1]) {
        continue;
      }

      taken[num - 1] = true;
      permutation.add(num);

      printPermutation(cnt + 1);

      permutation.remove(permutation.size() - 1);
      taken[num - 1] = false;
    }
  }

  private static void print(List<Integer> permutation) throws IOException {
    for (Integer num : permutation) {
      bw.write(String.valueOf(num));
      bw.write(' ');
    }
    bw.newLine();
  }

}
