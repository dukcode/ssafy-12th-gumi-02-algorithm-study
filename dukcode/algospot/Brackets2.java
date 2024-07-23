import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Stack;
import java.util.StringTokenizer;

public class Brackets2 {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    int c = Integer.parseInt(br.readLine());
    while (c-- > 0) {
      String line = br.readLine();

      boolean ok = true;
      Stack<Character> stk = new Stack<>();
      for (char ch : line.toCharArray()) {
        if (ch == '(' || ch == '{' || ch == '[') {
          stk.push(ch);
          continue;
        }

        if (stk.isEmpty() || !isPair(stk.peek(), ch)) {
          ok = false;
          break;
        }

        stk.pop();
      }

      bw.write(ok && stk.isEmpty() ? "YES" : "NO");
      bw.newLine();
    }

    br.close();
    bw.close();
  }

  private static boolean isPair(int left, int right) {
    if (left == '(' && right == ')') {
      return true;
    }

    if (left == '{' && right == '}') {
      return true;
    }

    return left == '[' && right == ']';
  }


}
