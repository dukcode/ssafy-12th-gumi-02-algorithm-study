import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class FigureOutTheTree2 {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;

  private static TrieNode root;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    n = Integer.parseInt(br.readLine());
    root = new TrieNode();
    for (int i = 0; i < n; i++) {
      st = new StringTokenizer(br.readLine());
      int k = Integer.parseInt(st.nextToken());

      List<String> route = new ArrayList<>();
      for (int idx = 0; idx < k; idx++) {
        route.add(st.nextToken());
      }

      root.insert(route);
    }

    StringBuilder sb = new StringBuilder();
    createAns(root, 0, sb);
    bw.write(sb.toString());

    br.close();
    bw.close();
  }

  private static void createAns(TrieNode node, int depth, StringBuilder sb) {
    for (int i = 0; i < 26; ++i) {
      if (node.children[i] == null) {
        continue;
      }

      for (int idx = 0; idx < depth; ++idx) {
        sb.append("--");
      }
      sb.append((char) (i + 'A'));
      sb.append("\n");
      createAns(node.children[i], depth + 1, sb);
    }
  }


  private static class TrieNode {

    TrieNode[] children;
    boolean isEnd;

    public TrieNode() {
      children = new TrieNode[26];
    }

    public void insert(List<String> route) {
      TrieNode cur = this;
      for (String v : route) {
        int idx = v.charAt(0) - 'A';
        if (cur.children[idx] == null) {
          cur.children[idx] = new TrieNode();
        }

        cur = cur.children[idx];
      }

      cur.isEnd = true;
    }
  }
}
