import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class FirstAppearNumber {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int m;

  private static int[] arr;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());

    arr = new int[n];
    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < n; ++i) {
      arr[i] = Integer.parseInt(st.nextToken());
    }

    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < m; ++i) {
      int target = Integer.parseInt(st.nextToken());
      int idx = findFirstTargetIdx(arr, target);
      bw.write(String.valueOf(idx < 0 ? idx : idx + 1));
      bw.newLine();
    }

    br.close();
    bw.close();
  }

  private static int findFirstTargetIdx(int[] arr, int target) {
    int idx = lowerBound(arr, target);
    return idx < arr.length && arr[idx] == target ? idx : -1;
  }

  private static int lowerBound(int[] arr, int target) {
    int st = 0;
    int en = arr.length;

    while (st < en) {
      int half = (st + en) / 2;
      if (arr[half] < target) {
        st = half + 1;
      } else {
        en = half;
      }
    }

    return st;
  }

}
