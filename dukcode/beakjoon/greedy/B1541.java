import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class B1541 {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    String input = br.readLine();
    boolean isMinus = false;
    if (input.startsWith("-")) {
      isMinus = true;
    }

    String[] nums = input.split("-");

    int result = 0;
    for (int i = 0; i < nums.length; i++) {
      int psum = calc(nums[i]);
      if (i == 0 && !isMinus) {
        result += psum;
      } else {
        result -= psum;
      }
    }

    bw.write(String.valueOf(result));

    br.close();
    bw.close();
  }

  private static int calc(String num) {
    int sum = 0;
    int n = 0;
    for (char ch : num.toCharArray()) {
      if (Character.isDigit(ch)) {
        n *= 10;
        n += ch - '0';
        continue;
      }

      sum += n;
      n = 0;
    }

    return sum + n;
  }

}
