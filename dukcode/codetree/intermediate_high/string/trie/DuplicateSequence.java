import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class DuplicateSequence {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;


  private static int n;
  private static String[] words;

  private static TrieNode root;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    root = new TrieNode();
    n = Integer.parseInt(br.readLine());
    words = new String[n];
    for (int i = 0; i < n; i++) {
      words[i] = br.readLine();
      root.insertWord(words[i]);
    }

    boolean ans = false;
    for (int i = 0; i < n; i++) {
      if (root.searchWord(words[i])) {
        ans = true;
        break;
      }
    }

    bw.write(String.valueOf(ans ? 0 : 1));

    br.close();
    bw.close();
  }


  private static class TrieNode {


    TrieNode[] children;
    boolean isEnd;

    public TrieNode() {
      isEnd = false;
      children = new TrieNode[10];
    }

    public void insertWord(String word) {
      TrieNode t = this;
      for (char c : word.toCharArray()) {
        int num = c - '0';

        if (t.children[num] == null) {
          t.children[num] = new TrieNode();
        }

        t = t.children[num];
      }

      t.isEnd = true;
    }

    public boolean searchWord(String word) {
      TrieNode t = this;
      for (char c : word.toCharArray()) {
        if (t.isEnd) {
          return true;
        }

        int num = c - '0';
        if (t.children[num] == null) {
          break;
        }
        t = t.children[num];
      }

      return false;
    }
  }
}
