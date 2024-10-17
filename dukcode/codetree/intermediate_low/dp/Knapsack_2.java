import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Knapsack_2 {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int maxWeight;

  private static Jewel[] jewels;

  private static int[] cache;

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

    cache = new int[maxWeight + 1];
    Arrays.fill(cache, -1);
    cache[0] = 0;

    for (Jewel jewel : jewels) {
      for (int w = maxWeight; w >= jewel.weight; w--) {
        cache[w] = Math.max(cache[w], cache[w - jewel.weight] + jewel.value);
      }
    }

    bw.write(String.valueOf(Arrays.stream(cache).max().getAsInt()));

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
