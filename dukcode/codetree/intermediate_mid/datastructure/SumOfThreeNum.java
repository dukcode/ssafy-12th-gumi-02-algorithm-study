import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class SumOfThreeNum {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int k;

  private static int[] arr;
  private static Map<Integer, Integer> freq;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    k = Integer.parseInt(st.nextToken());

    arr = new int[n];
    freq = new HashMap<>();
    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < n; i++) {
      int num = Integer.parseInt(st.nextToken());
      arr[i] = num;
      freq.put(num, freq.getOrDefault(num, 0) + 1);
    }

    int ans = 0;
    for (int num : arr) {
      freq.computeIfPresent(num, (k, v) -> v == 0 ? 0 : v - 1);
      int counter = k - num;
      for (int second : freq.keySet()) {
        int third = counter - second;
        if (third == second) {
          ans += freq.get(second) * (freq.get(second) - 1);
          continue;
        }

        ans += freq.get(second) * freq.getOrDefault(third, 0);
      }
    }

    bw.write(String.valueOf(ans / 2));

    br.close();
    bw.close();
  }

}
