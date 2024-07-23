import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Traversal {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int[] preorder;
  private static int[] inorder;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    int c = Integer.parseInt(br.readLine());
    while (c-- > 0) {
      n = Integer.parseInt(br.readLine());

      preorder = new int[n];
      st = new StringTokenizer(br.readLine());
      for (int i = 0; i < n; ++i) {
        preorder[i] = Integer.parseInt(st.nextToken());
      }

      inorder = new int[n];
      st = new StringTokenizer(br.readLine());
      for (int i = 0; i < n; ++i) {
        inorder[i] = Integer.parseInt(st.nextToken());
      }

      List<Integer> postorder = new ArrayList<Integer>();
      postorder(postorder, 0, n, 0, n);

      for (Integer num : postorder) {
        bw.write(String.valueOf(num));
        bw.write(' ');
      }
      bw.newLine();
    }

    br.close();
    bw.close();
  }

  private static void postorder(List<Integer> postorder, int ps, int pe, int is, int ie) {
    int size = pe - ps;

    if (size == 0) {
      return;
    }

    int root = preorder[ps];

    int rootIdx = -1;
    for (int i = is; i < ie; ++i) {
      if (root == inorder[i]) {
        rootIdx = i;
        break;
      }
    }

    int leftSize = rootIdx - is;

    postorder(postorder, ps + 1, ps + 1 + leftSize, is, rootIdx);
    postorder(postorder, ps + 1 + leftSize, pe, rootIdx + 1, ie);
    postorder.add(root);
  }


}
