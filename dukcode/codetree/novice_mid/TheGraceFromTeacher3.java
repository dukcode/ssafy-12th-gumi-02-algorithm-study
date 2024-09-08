import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.StringTokenizer;

public class TheGraceFromTeacher3 {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    int n = Integer.parseInt(st.nextToken());
    int b = Integer.parseInt(st.nextToken());

    int[] cost = new int[n];
    int[] discounted = new int[n];
    for (int i = 0; i < n; i++) {
      st = new StringTokenizer(br.readLine());
      int p = Integer.parseInt(st.nextToken());
      int s = Integer.parseInt(st.nextToken());

      cost[i] = p + s;
      discounted[i] = p / 2 + s;

    }

    int maxCount = 0;
    for (int i = 0; i < n; ++i) {
      maxCount = Math.max(maxCount, getCnt(cost, discounted, i, b));
    }

    bw.write(String.valueOf(maxCount));

    br.close();
    bw.close();
  }

  private static int getCnt(int[] cost, int[] discounted, int idx, int budget) {
    int n = cost.length;
    List<Integer> price = new ArrayList<>();
    for (int i = 0; i < n; ++i) {
      if (i == idx) {
        price.add(discounted[i]);
        continue;
      }

      price.add(cost[i]);
    }

    price.sort(Comparator.naturalOrder());

    int sum = 0;
    for (int i = 0; i < n; ++i) {
      sum += price.get(i);
      if (sum > budget) {
        return i;
      }
    }

    return 0;
  }

}
