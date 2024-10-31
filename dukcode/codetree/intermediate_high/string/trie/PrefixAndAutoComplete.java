import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringJoiner;
import java.util.StringTokenizer;

public class PrefixAndAutoComplete {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static String[] words;

  private static TrieNode root;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    n = Integer.parseInt(br.readLine());
    words = new String[n];
    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < n; ++i) {
      words[i] = st.nextToken();
    }

    root = new TrieNode();
    for (int i = 0; i < n; ++i) {
      root.insert(words[i]);
    }

    StringJoiner sj = new StringJoiner(" ");
    for (int i = 0; i < n; ++i) {
      sj.add(String.valueOf(root.autoComplete(words[i])));
    }

    bw.write(sj.toString());

    br.close();
    bw.close();
  }

  private static class TrieNode {

    TrieNode[] children = new TrieNode[26];
    int cnt = 0;
    boolean isEnd = false;

    public void insert(String word) {
      TrieNode cur = this;
      for (char c : word.toCharArray()) {
        int idx = c - 'a';
        if (cur.children[idx] == null) {
          cur.children[idx] = new TrieNode();
          cur.cnt++;
        }
        cur = cur.children[idx];
      }

      cur.isEnd = true;
    }

    private int autoComplete(String word) {
      TrieNode cur = this;
      int ret = 0;
      for (int i = 0; i < word.length(); ++i) {
        int idx = word.charAt(i) - 'a';

        if (cur == root || cur.isEnd || cur.cnt > 1) {
          ret++;
        }

        cur = cur.children[idx];
      }

      return ret;
    }
  }


}
