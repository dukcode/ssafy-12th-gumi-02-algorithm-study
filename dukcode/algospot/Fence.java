import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Stack;
import java.util.StringTokenizer;

public class Fence {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int[] arr;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    int c = Integer.parseInt(br.readLine());
    while (c-- > 0) {
      n = Integer.parseInt(br.readLine());

      arr = new int[n + 1];
      st = new StringTokenizer(br.readLine());
      for (int i = 0; i < n; i++) {
        arr[i] = Integer.parseInt(st.nextToken());
      }

      int maxArea = 0;
      Stack<Integer> stk = new Stack<>();
      for (int idx = 0; idx <= n; ++idx) {
        while (!stk.isEmpty() && arr[stk.peek()] > arr[idx]) {
          int h = arr[stk.pop()];
          int left = stk.isEmpty() ? -1 : stk.peek();
          int right = idx;
          maxArea = Math.max(maxArea, h * (right - left - 1));
        }

        stk.push(idx);
      }

      bw.write(String.valueOf(maxArea));
      bw.newLine();
    }

    br.close();
    bw.close();
  }


}
