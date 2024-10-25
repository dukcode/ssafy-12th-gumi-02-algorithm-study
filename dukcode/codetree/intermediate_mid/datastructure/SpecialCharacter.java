import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class SpecialCharacter {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    char[] word = br.readLine().toCharArray();
    Map<Character, Integer> freq = new HashMap<>();
    for (char c : word) {
      freq.put(c, freq.getOrDefault(c, 0) + 1);
    }

    String ans = "None";
    for (char c : word) {
      if (freq.get(c) == 1) {
        ans = String.valueOf(c);
        break;
      }
    }

    bw.write(ans);

    br.close();
    bw.close();
  }

}
