import java.io.IOException;
import java.util.Scanner;

public class StrangeFlippingTile {

  private static final int MX = 100_000;
  private static final int WHITE = -1;
  private static final int BLACK = 1;

  private static int[] arr;

  public static void main(String[] args) throws IOException {
    Scanner sc = new Scanner(System.in);

    // -100_000 ~ 100_000
    arr = new int[2 * MX + 1];

    int n = sc.nextInt();
    int idx = MX;
    for (int i = 0; i < n; ++i) {
      int cnt = sc.nextInt();
      int dir = sc.next().equals("R") ? BLACK : WHITE;

      arr[idx] = dir;
      cnt--;

      while (cnt-- > 0) {
        idx += dir;
        arr[idx] = dir;
      }

    }

    int cntBlack = 0;
    int cntWhite = 0;
    for (int i = 0; i < 2 * MX + 1; ++i) {
      if (arr[i] == BLACK) {
        cntBlack++;
      } else if (arr[i] == WHITE) {
        cntWhite++;
      }
    }

    System.out.println(cntWhite + " " + cntBlack);

  }

}
