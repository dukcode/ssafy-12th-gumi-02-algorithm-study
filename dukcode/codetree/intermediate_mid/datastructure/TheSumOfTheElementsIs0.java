import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class TheSumOfTheElementsIs0 {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int[][] arr;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    n = Integer.parseInt(br.readLine());

    arr = new int[4][n];
    for (int i = 0; i < 4; i++) {
      st = new StringTokenizer(br.readLine());
      for (int idx = 0; idx < n; idx++) {
        arr[i][idx] = Integer.parseInt(st.nextToken());
      }
    }

    Map<Integer, Integer> sum1 = getSum(0, 1);
    Map<Integer, Integer> sum2 = getSum(2, 3);

    int ans = 0;
    for (int num : sum1.keySet()) {
      if (sum2.containsKey(-num)) {
        ans += sum1.get(num) * sum2.get(-num);
      }
    }

    bw.write(String.valueOf(ans));

    br.close();
    bw.close();
  }

  private static Map<Integer, Integer> getSum(int first, int second) {
    Map<Integer, Integer> ret = new HashMap<>();
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        int sum = arr[first][i] + arr[second][j];
        ret.put(sum, ret.getOrDefault(sum, 0) + 1);
      }
    }

    return ret;
  }


}
