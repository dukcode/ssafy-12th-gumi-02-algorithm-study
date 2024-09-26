import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class B14999 {

  private static final int[] dy = {0, 0, -1, 1};
  private static final int[] dx = {1, -1, 0, 0};

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int h;
  private static int w;
  private static int y;
  private static int x;
  private static int k;

  private static int[][] board;
  private static int[][] dice;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    dice = new int[][]{
        {0, 0, 0},
        {0, 0, 0},
        {0, 0, 0},
        {0, 0, 0}
    };

    st = new StringTokenizer(br.readLine());
    h = Integer.parseInt(st.nextToken());
    w = Integer.parseInt(st.nextToken());
    y = Integer.parseInt(st.nextToken());
    x = Integer.parseInt(st.nextToken());
    k = Integer.parseInt(st.nextToken());

    board = new int[h][w];
    for (int y = 0; y < h; ++y) {
      st = new StringTokenizer(br.readLine());
      for (int x = 0; x < w; ++x) {
        board[y][x] = Integer.parseInt(st.nextToken());
      }
    }

    List<Integer> ans = new ArrayList<>();
    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < k; ++i) {
      int dir = Integer.parseInt(st.nextToken()) - 1;
      int ny = y + dy[dir];
      int nx = x + dx[dir];

      if (ny < 0 || ny >= h || nx < 0 || nx >= w) {
        continue;
      }

      y = ny;
      x = nx;

      rotate(dir);

      if (board[y][x] == 0) {
        board[y][x] = dice[3][1];
      } else {
        dice[3][1] = board[y][x];
        board[y][x] = 0;
      }

      ans.add(dice[1][1]);
    }

    for (Integer top : ans) {
      bw.write(String.valueOf(top));
      bw.newLine();
    }

    br.close();
    bw.close();

  }

  private static void print() {
    for (int y = 0; y < 4; ++y) {
      System.out.println(Arrays.toString(dice[y]));
    }
    System.out.println();
  }

  private static void rotate(int dir) {
    int tmp;
    switch (dir) {
      case 0: // 동
        tmp = dice[3][1];
        dice[3][1] = dice[1][2];
        dice[1][2] = dice[1][1];
        dice[1][1] = dice[1][0];
        dice[1][0] = tmp;
        break;
      case 1: // 서
        tmp = dice[3][1];
        dice[3][1] = dice[1][0];
        dice[1][0] = dice[1][1];
        dice[1][1] = dice[1][2];
        dice[1][2] = tmp;
        break;
      case 2: // 북
        tmp = dice[0][1];
        dice[0][1] = dice[1][1];
        dice[1][1] = dice[2][1];
        dice[2][1] = dice[3][1];
        dice[3][1] = tmp;
        break;
      case 3: // 남
        tmp = dice[3][1];
        dice[3][1] = dice[2][1];
        dice[2][1] = dice[1][1];
        dice[1][1] = dice[0][1];
        dice[0][1] = tmp;
        break;
      default:
        break;
    }
  }

}
