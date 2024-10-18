import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Knapsack_1 {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int maxWeight;

  private static Jewel[] jewels;

  private static int[][] cache;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    maxWeight = Integer.parseInt(st.nextToken());

    jewels = new Jewel[n];
    for (int i = 0; i < n; i++) {
      st = new StringTokenizer(br.readLine());
      int weight = Integer.parseInt(st.nextToken());
      int value = Integer.parseInt(st.nextToken());
      jewels[i] = new Jewel(weight, value);
    }

    cache = new int[n][maxWeight + 1];

    for (int y = 0; y < n; y++) {
      Arrays.fill(cache[y], -1);
    }

    bw.write(String.valueOf(solve(n - 1, maxWeight)));

    br.close();
    bw.close();
  }

  private static int solve(int idx, int weight) {
    if (idx < 0) {
      return 0;
    }

    if (cache[idx][weight] != -1) {
      return cache[idx][weight];
    }

    int ret = solve(idx - 1, weight);
    if (weight - jewels[idx].weight >= 0) {
      ret = Math.max(ret, solve(idx - 1, weight - jewels[idx].weight) + jewels[idx].value);
    }

    return cache[idx][weight] = ret;
  }

  private static class Jewel {

    int weight;
    int value;

    public Jewel(int weight, int value) {
      this.weight = weight;
      this.value = value;
    }
  }


}
