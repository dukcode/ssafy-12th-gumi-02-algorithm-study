import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class CorrespondingNumbersAndCharacters {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int m;

  private static Map<String, String> wordToNumMap;
  private static Map<String, String> numToWordMap;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());

    wordToNumMap = new HashMap<>();
    numToWordMap = new HashMap<>();
    for (int i = 1; i <= n; i++) {
      String word = br.readLine();

      wordToNumMap.put(word, String.valueOf(i));
      numToWordMap.put(String.valueOf(i), word);
    }

    for (int i = 0; i < m; i++) {
      String c = br.readLine();

      if (wordToNumMap.containsKey(c)) {
        bw.write(wordToNumMap.get(c));
      } else {
        bw.write(numToWordMap.get(c));
      }

      bw.newLine();
    }

    br.close();
    bw.close();
  }


}
