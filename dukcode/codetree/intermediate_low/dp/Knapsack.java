import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Knapsack {

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

    cache = new int[n + 1][maxWeight + 1];

    for (int y = 1; y <= n; y++) {
      Arrays.fill(cache[y], -1);
    }

    for (int idx = 1; idx <= n; ++idx) {
      for (int w = 0; w <= maxWeight; w++) {

        cache[idx][w] = cache[idx - 1][w];

        if (w - jewels[idx - 1].weight >= 0) {
          cache[idx][w] = Math.max(cache[idx][w],
              cache[idx - 1][w - jewels[idx - 1].weight] + jewels[idx - 1].value);
        }

      }
    }

    bw.write(String.valueOf(cache[n][maxWeight]));

    br.close();
    bw.close();
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
