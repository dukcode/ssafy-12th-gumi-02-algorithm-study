import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.text.StringCharacterIterator;

public class QuadTree {

  private static BufferedReader br;
  private static BufferedWriter bw;
  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    int c = Integer.parseInt(br.readLine());
    while (c-- > 0) {
      String compressed = br.readLine();
      StringCharacterIterator it = new StringCharacterIterator(compressed);
      String reversed = reverse(it);
      bw.write(reversed);
      bw.newLine();
    }

    br.close();
    bw.close();
  }

  private static String reverse(StringCharacterIterator it) {
    char head = it.current();
    it.next();

    if (head != 'x') {
      return String.valueOf(head);
    }

    String leftUpper = reverse(it);
    String rightUpper = reverse(it);
    String leftLower = reverse(it);
    String rightLower = reverse(it);

    return "x" + leftLower + rightLower + leftUpper + rightUpper;
  }
}