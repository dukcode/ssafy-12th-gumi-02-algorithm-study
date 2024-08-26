import java.util.Scanner;

public class ContinuouslyOverlappingSquares {

  private static final int MX = 100;
  private static final int SIZE = 2 * MX + 1;

  private static final int BLUE = 1;
  private static final int RED = 2;

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();

    int[][] board = new int[SIZE][SIZE];

    for (int i = 0; i < n; ++i) {
      int x1 = sc.nextInt() + 100;
      int y1 = sc.nextInt() + 100;
      int x2 = sc.nextInt() + 100;
      int y2 = sc.nextInt() + 100;

      int color = i % 2 == 0 ? RED : BLUE;

      for (int y = y1; y < y2; ++y) {
        for (int x = x1; x < x2; ++x) {
          board[y][x] = color;
        }
      }

    }

    int cntBlue = 0;
    for (int y = 0; y < SIZE; y++) {
      for (int x = 0; x < SIZE; x++) {
        if (board[y][x] == BLUE) {
          cntBlue++;
        }
      }
    }

    System.out.println(cntBlue);
  }

}
