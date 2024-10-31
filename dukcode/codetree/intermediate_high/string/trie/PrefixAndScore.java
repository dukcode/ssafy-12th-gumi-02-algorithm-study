import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class PrefixAndScore {

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
    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < n; i++) {
      root.insert(st.nextToken());
    }

    bw.write(String.valueOf(solve(root, 0)));

    br.close();
    bw.close();
  }

  private static int solve(TrieNode cur, int depth) {
    int ret = cur.cnt * depth;
    for (TrieNode child : cur.children) {
      if (child == null) {
        continue;
      }

      ret = Math.max(ret, solve(child, depth + 1));
    }

    return ret;
  }

  private static class TrieNode {

    TrieNode[] children = new TrieNode[26];
    int cnt = 0;

    public void insert(String word) {
      TrieNode cur = this;
      for (char c : word.toCharArray()) {
        int idx = c - 'a';
        if (cur.children[idx] == null) {
          cur.children[idx] = new TrieNode();
        }

        cur = cur.children[idx];
        cur.cnt++;
      }
    }
  }

}
