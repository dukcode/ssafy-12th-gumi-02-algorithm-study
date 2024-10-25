import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Map;
import java.util.Map.Entry;
import java.util.StringTokenizer;
import java.util.TreeMap;

public class WordList {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    int n = Integer.parseInt(br.readLine());
    Map<String, Integer> freq = new TreeMap<>();
    for (int i = 0; i < n; i++) {
      String word = br.readLine();
      freq.put(word, freq.getOrDefault(word, 0) + 1);
    }

    for (Entry<String, Integer> e : freq.entrySet()) {
      bw.write(e.getKey() + " " + e.getValue() + "\n");
    }

    br.close();
    bw.close();
  }


}
