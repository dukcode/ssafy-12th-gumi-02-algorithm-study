import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class IndicesOfSortedArray {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static Number[] arr;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    n = Integer.parseInt(br.readLine());

    arr = new Number[n];
    st = new StringTokenizer(br.readLine());

    for (int idx = 1; idx <= n; ++idx) {
      arr[idx - 1] = new Number(idx, Integer.parseInt(st.nextToken()));
    }

    Arrays.sort(arr);

    int[] lastPos = new int[n];
    for (int i = 0; i < n; ++i) {
      lastPos[arr[i].idx - 1] = i + 1;
    }

    for (int i = 0; i < n; ++i) {
      bw.write(String.valueOf(lastPos[i]));
      bw.write(' ');
    }
    bw.newLine();

    br.close();
    bw.close();

  }

  private static class Number implements Comparable<Number> {

    int idx;
    int num;

    public Number(int idx, int num) {
      this.idx = idx;
      this.num = num;
    }

    @Override
    public int compareTo(Number o) {
      if (this.num == o.num) {
        return Integer.compare(this.idx, o.idx);
      }

      return Integer.compare(this.num, o.num);
    }
  }

}
