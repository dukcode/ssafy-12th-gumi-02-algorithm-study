import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class IncDecSorting {

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
    print();

    Integer[] integerArr = Arrays.stream(arr).boxed().toArray(Integer[]::new);
    Arrays.sort(integerArr, Collections.reverseOrder());
    arr = Arrays.stream(integerArr).mapToInt(i -> i).toArray();
    print();

    br.close();
    bw.close();

  }

  private static void print() throws IOException {
    for (int i = 0; i < n; i++) {
      bw.write(String.valueOf(arr[i]));
      bw.write(' ');
    }
    bw.newLine();
  }

}
