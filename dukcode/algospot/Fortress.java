import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class Fortress {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int[] x;
  private static int[] y;
  private static int[] r;

  private static int longest;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    int c = Integer.parseInt(br.readLine());
    while (c-- > 0) {
      n = Integer.parseInt(br.readLine());

      x = new int[n];
      y = new int[n];
      r = new int[n];
      for (int i = 0; i < n; i++) {
        st = new StringTokenizer(br.readLine());
        x[i] = Integer.parseInt(st.nextToken());
        y[i] = Integer.parseInt(st.nextToken());
        r[i] = Integer.parseInt(st.nextToken());
      }

      longest = 0;
      TreeNode root = getTree(0);
      int ans = getLongest(root);
      bw.write(String.valueOf(ans));
      bw.newLine();
    }

    br.close();
    bw.close();
  }

  private static TreeNode getTree(int root) {
    TreeNode ret = new TreeNode();
    for (int ch = 0; ch < n; ++ch) {
      if (isChild(root, ch)) {
        ret.children.add(getTree(ch));
      }
    }

    return ret;
  }

  private static int square(int a) {
    return a * a;
  }

  private static boolean enclose(int p, int c) {
    return r[p] > r[c] && (square(x[p] - x[c]) + square(y[p] - y[c])) < square(r[p] - r[c]);
  }

  private static boolean isChild(int parent, int child) {
    if (!enclose(parent, child)) {
      return false;
    }

    for (int i = 0; i < n; ++i) {
      if (i == parent || i == child) {
        continue;
      }

      if (enclose(parent, i) && enclose(i, child)) {
        return false;
      }
    }

    return true;
  }

  private static int getLongest(TreeNode root) {
    int height = height(root);
    return Math.max(height, longest);
  }

  private static int height(TreeNode root) {

    List<Integer> heights = new ArrayList<>();
    for (TreeNode child : root.children) {
      heights.add(height(child));
    }

    if (heights.isEmpty()) {
      return 0;
    }

    Collections.sort(heights);

    if (heights.size() >= 2) {
      longest = Math.max(longest,
          heights.get(heights.size() - 2) + heights.get(heights.size() - 1) + 2);
    }

    return heights.get(heights.size() - 1) + 1;
  }

  private static class TreeNode {

    List<TreeNode> children = new ArrayList<>();
  }

}
