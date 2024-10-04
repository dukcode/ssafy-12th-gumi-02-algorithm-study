import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Jenga1D {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int[] blocks;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    n = Integer.parseInt(br.readLine());

    blocks = new int[n];
    for (int i = 0; i < n; i++) {
      blocks[i] = Integer.parseInt(br.readLine());
    }

    for (int i = 0; i < 2; ++i) {
      st = new StringTokenizer(br.readLine());
      int fr = Integer.parseInt(st.nextToken()) - 1;
      int to = Integer.parseInt(st.nextToken()) - 1;

      remove(fr, to);
    }

    bw.write(String.valueOf(blocks.length));
    bw.newLine();

    for (int i = 0; i < blocks.length; ++i) {
      bw.write(String.valueOf(blocks[i]));
      bw.newLine();
    }

    br.close();
    bw.close();
  }

  private static void remove(int fr, int to) {
    int[] tmp = new int[blocks.length - (to - fr + 1)];
    int idx = 0;

    for (int i = 0; i < blocks.length; ++i) {
      if (fr <= i && i <= to) {
        continue;
      }
      tmp[idx++] = blocks[i];
    }

    blocks = tmp;
  }


}
