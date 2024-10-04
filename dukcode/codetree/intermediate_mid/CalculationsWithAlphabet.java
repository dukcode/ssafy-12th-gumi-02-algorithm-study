import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class CalculationsWithAlphabet {

  private static BufferedReader br;
  private static BufferedWriter bw;

  private static char[] expression;
  private static int[] nums;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    expression = br.readLine().toCharArray();
    nums = new int[6];
    bw.write(String.valueOf(solve(0)));

    br.close();
    bw.close();

  }

  private static long solve(int idx) {
    if (idx == 6) {
      return calculate();
    }

    long ret = Long.MIN_VALUE;
    for (int i = 1; i <= 4; ++i) {
      nums[idx] = i;
      ret = Math.max(ret, solve(idx + 1));
    }

    return ret;
  }

  private static long calculate() {
    long res = 0;
    char op = '+';
    for (char token : expression) {
      if (!Character.isAlphabetic(token)) {
        op = token;
        continue;
      }

      switch (op) {
        case '+':
          res += nums[token - 'a'];
          break;
        case '*':
          res *= nums[token - 'a'];
          break;
        case '-':
          res -= nums[token - 'a'];
          break;
      }
    }

    return res;
  }

}
