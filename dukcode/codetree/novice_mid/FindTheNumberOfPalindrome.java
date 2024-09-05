import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class FindTheNumberOfPalindrome {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    int x = Integer.parseInt(st.nextToken());
    int y = Integer.parseInt(st.nextToken());

    int cnt = 0;
    for (int num = x; num <= y; num++) {
      if (isPalindrome(num)) {
        cnt++;
      }
    }

    bw.write(String.valueOf(cnt));

    br.close();
    bw.close();
  }

  private static boolean isPalindrome(int num) {
    String strNum = String.valueOf(num);

    int st = 0;
    int en = strNum.length() - 1;

    while (st < en) {
      if (strNum.charAt(st++) != strNum.charAt(en--)) {
        return false;
      }
    }

    return true;
  }

}
