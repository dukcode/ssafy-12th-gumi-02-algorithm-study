import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class GroupSameWord {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static Map<String, Integer> freq;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    n = Integer.parseInt(br.readLine());

    freq = new HashMap<>();
    for (int i = 0; i < n; ++i) {
      char[] word = br.readLine().toCharArray();
      Arrays.sort(word);
      String sortedWord = String.valueOf(word);

      freq.put(sortedWord, freq.getOrDefault(sortedWord, 0) + 1);
    }

    PriorityQueue<Integer> values = new PriorityQueue<>(Comparator.reverseOrder());
    values.addAll(freq.values());

    bw.write(String.valueOf(values.poll()));

    br.close();
    bw.close();
  }


}
