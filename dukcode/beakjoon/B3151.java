import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class B3151 {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int[] arr;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    n = Integer.parseInt(br.readLine());

    arr = new int[n];

    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < n; i++) {
      arr[i] = Integer.parseInt(st.nextToken());
    }

    Arrays.sort(arr);

    long cnt = 0;
    for (int i = 0; i < n; i++) {
      for (int j = i + 1; j < n; j++) {
        int target = -arr[i] - arr[j];

        int st = lowerBound(arr, target, j + 1, n);
        int en = upperBound(arr, target, j + 1, n);

        cnt += en - st;
      }
    }

    bw.write(String.valueOf(cnt));

    br.close();
    bw.close();
  }

  private static int lowerBound(int[] arr, int target, int st, int en) {
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

  private static int upperBound(int[] arr, int target, int st, int en) {
    while (st < en) {
      int half = (st + en) / 2;

      if (arr[half] <= target) {
        st = half + 1;
      } else {
        en = half;
      }

    }

    return st;
  }


}
