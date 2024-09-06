import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class NumberOfIntegers {

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
    for (int i = 0; i < n; i++) {
      arr[i] = Integer.parseInt(st.nextToken());
    }

    for (int i = 0; i < m; i++) {
      int target = Integer.parseInt(br.readLine());
      int cnt = countTarget(arr, target);
      bw.write(String.valueOf(cnt));
      bw.newLine();
    }

    br.close();
    bw.close();
  }

  private static int countTarget(int[] arr, int target) {
    return upperBound(arr, target) - lowerBound(arr, target);
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

  private static int upperBound(int[] arr, int target) {
    int st = 0;
    int en = arr.length;

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
