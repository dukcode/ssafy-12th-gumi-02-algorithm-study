import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Queue;

public class NewAlphabet {

  private static BufferedReader br;
  private static BufferedWriter bw;

  private static int n;
  private static String[] words;

  private static int numAlpha;
  private static Map<Character, Integer> alphaToIdx;
  private static char[] idxToAlpha;

  private static List<Integer>[] adj;
  private static int[] inDegrees;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    n = Integer.parseInt(br.readLine());

    words = new String[n];
    for (int i = 0; i < n; i++) {
      words[i] = br.readLine();
    }

    numAlpha = 0;
    alphaToIdx = new HashMap<>();
    idxToAlpha = new char[26];
    for (String word : words) {
      for (char c : word.toCharArray()) {
        if (alphaToIdx.containsKey(c)) {
          continue;
        }

        alphaToIdx.put(c, numAlpha);
        idxToAlpha[numAlpha] = c;
        numAlpha++;
      }
    }

    makeGraph();

    Queue<Integer> q = new ArrayDeque<>();
    for (int i = 0; i < numAlpha; i++) {
      if (inDegrees[i] == 0) {
        q.offer(i);
      }
    }

    List<Character> order = new ArrayList<>();
    boolean[] vis = new boolean[numAlpha];
    int cntVis = 0;
    boolean isInf = false;

    Loop:
    while (!q.isEmpty()) {
      if (q.size() >= 2) {
        isInf = true;
      }
      int here = q.poll();
      vis[here] = true;
      cntVis++;
      order.add(idxToAlpha[here]);
      for (int there : adj[here]) {
        if (vis[there]) {
          break Loop;
        }

        inDegrees[there]--;
        if (inDegrees[there] != 0) {
          continue;
        }

        q.offer(there);
      }
    }

    boolean isImpossible = cntVis != numAlpha;

    if (isImpossible) {
      bw.write("-1");
    } else if (isInf) {
      bw.write("inf");
    } else {
      for (char c : order) {
        bw.write(c);
      }
    }

    br.close();
    bw.close();
  }

  private static void makeGraph() {
    adj = new List[numAlpha];
    for (int i = 0; i < numAlpha; i++) {
      adj[i] = new ArrayList<>();
    }

    inDegrees = new int[numAlpha];
    for (int i = 1; i < n; ++i) {
      String word1 = words[i - 1];
      String word2 = words[i];

      int len = Math.min(word1.length(), word2.length());
      for (int idx = 0; idx < len; ++idx) {
        char a = word1.charAt(idx);
        char b = word2.charAt(idx);
        if (a != b) {

          adj[alphaToIdx.get(a)].add(alphaToIdx.get(b));

          inDegrees[alphaToIdx.get(b)]++;

          break;
        }
      }
    }
  }


}
