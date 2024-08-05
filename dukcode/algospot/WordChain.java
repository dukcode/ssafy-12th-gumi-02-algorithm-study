import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class WordChain {

  private static final int NUM_ALPHABETS = 26;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static String[] words;

  private static int[][] adj;
  private static int[] inDegrees;
  private static int[] outDegrees;
  private static Queue<String>[][] graph;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    int c = Integer.parseInt(br.readLine());
    while (c-- > 0) {
      n = Integer.parseInt(br.readLine());
      words = new String[n];
      for (int i = 0; i < n; i++) {
        words[i] = br.readLine();
      }

      graph = new Queue[NUM_ALPHABETS][NUM_ALPHABETS];
      for (int y = 0; y < NUM_ALPHABETS; ++y) {
        for (int x = 0; x < NUM_ALPHABETS; ++x) {
          graph[y][x] = new ArrayDeque<>();
        }
      }

      adj = new int[NUM_ALPHABETS][NUM_ALPHABETS];
      inDegrees = new int[NUM_ALPHABETS];
      outDegrees = new int[NUM_ALPHABETS];
      for (String word : words) {
        int len = word.length();
        int from = word.charAt(0) - 'a';
        int to = word.charAt(len - 1) - 'a';

        graph[from][to].offer(word);
        adj[from][to]++;
        inDegrees[to]++;
        outDegrees[from]++;
      }


      List<String> order = solve();
      if (order.isEmpty()) {
        bw.write("IMPOSSIBLE");
      } else {
        for (String word : order) {
          bw.write(word);
          bw.write(' ');
        }
      }
      bw.newLine();
    }

    br.close();
    bw.close();
  }

  private static boolean isEuler() {
    int plus1 = 0;
    int minus1 = 0;

    for (int i = 0; i < NUM_ALPHABETS; i++) {
      int delta = outDegrees[i] - inDegrees[i];
      if (delta < -1 || delta > 1) {
        return false;
      }

      if (delta == 1) {
        plus1++;
      }

      if (delta == -1) {
        minus1++;
      }
    }

    return (plus1 == 0 && minus1 == 0) || (plus1 == 1 && minus1 == 1);
  }

  private static List<String> solve() {
    if (!isEuler()) {
      return Collections.emptyList();
    }

    List<Integer> circuit =  getEulerCircuitOrTrail();

    if (circuit.size() == n) {
      return Collections.emptyList();
    }

    Collections.reverse(circuit);

    List<String> ret = new ArrayList<>();
    for (int i = 1; i < circuit.size(); i++) {
      ret.add(graph[circuit.get(i - 1)][circuit.get(i)].poll());
    }

    return ret;
  }

  private static void getEulerCircuit(int here, List<Integer> circuit) {
    for (int there = 0; there < NUM_ALPHABETS; ++there) {
      while (adj[here][there] > 0) {
        adj[here][there]--;
        getEulerCircuit(there, circuit);
      }
    }

    circuit.add(here);
  }

  private static List<Integer> getEulerCircuitOrTrail() {
    List<Integer> ret = new ArrayList<>();

    for (int i = 0; i < NUM_ALPHABETS; ++i) {
      if (outDegrees[i] == inDegrees[i] + 1) {
        getEulerCircuit(i, ret);
        return ret;
      }

    }

    for (int i = 0; i < NUM_ALPHABETS; ++i) {
      if (outDegrees[i] != 0) {
        getEulerCircuit(i, ret);
        return ret;
      }

    }

    return ret;
  }


}
