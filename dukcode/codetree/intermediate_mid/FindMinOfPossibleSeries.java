import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;

public class FindMinOfPossibleSeries {

  private static BufferedReader br;
  private static BufferedWriter bw;

  private static int n;
  private static List<Character> word;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    n = Integer.parseInt(br.readLine());
    word = new ArrayList<>();
    solve(word);

    for (char c : word) {
      bw.write(c);
    }
    bw.newLine();

    br.close();
    bw.close();
  }

  private static boolean solve(List<Character> word) {
    if (word.size() == n) {
      return true;
    }

    for (char c = '4'; c <= '6'; c++) {
      word.add(c);
      if (!isValid(word)) {
        word.remove(word.size() - 1);
        continue;
      }

      if (solve(word)) {
        return true;
      }

      word.remove(word.size() - 1);
    }

    return false;
  }

  private static boolean isValid(List<Character> word) {
    int n = word.size();
    for (int len = 1; len <= n / 2; ++len) {
      if (lastLenEquals(word, len)) {
        return false;
      }
    }
    return true;
  }

  private static boolean lastLenEquals(List<Character> word, int len) {
    int n = word.size();

    for (int i = 0; i < len; ++i) {
      if (word.get(n - 1 - i) != word.get(n - 1 - i - len)) {
        return false;
      }
    }

    return true;
  }

}
