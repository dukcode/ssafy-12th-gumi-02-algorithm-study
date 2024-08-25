import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class B14503 {

  // 북, 동, 남, 서
  // 시계: +1, 반시계: -1
  private static final int[] dy = {-1, 0, 1, 0};
  private static final int[] dx = {0, 1, 0, -1};

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int h;
  private static int w;

  private static int[][] board;

  private static int ry;
  private static int rx;
  private static int dir;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    h = Integer.parseInt(st.nextToken());
    w = Integer.parseInt(st.nextToken());

    st = new StringTokenizer(br.readLine());
    ry = Integer.parseInt(st.nextToken());
    rx = Integer.parseInt(st.nextToken());
    dir = Integer.parseInt(st.nextToken());

    board = new int[h][w];
    for (int y = 0; y < h; y++) {
      st = new StringTokenizer(br.readLine());
      for (int x = 0; x < w; x++) {
        board[y][x] = Integer.parseInt(st.nextToken());
      }
    }

    int cnt = 0;
    Loop:
    while (true) {
      if (board[ry][rx] == 0) {
        board[ry][rx] = -1;
        cnt++;
      }

      for (int i = 0; i < 4; ++i) {
        dir = (dir + 3) % 4;
        int nry = ry + dy[dir];
        int nrx = rx + dx[dir];

        if (nry < 0 || nry >= h || nrx < 0 || nrx >= w) {
          continue;
        }

        if (board[nry][nrx] == 0) {
          ry = nry;
          rx = nrx;
          continue Loop;
        }
      }

      int backDir = (dir + 2) % 4;
      int nry = ry + dy[backDir];
      int nrx = rx + dx[backDir];

      if ((nry < 0 || nrx < 0 || nry >= h || nrx >= w) || board[nry][nrx] == 1) {
        break;
      }

      ry = nry;
      rx = nrx;
    }

    bw.write(String.valueOf(cnt));

    br.close();
    bw.close();

  }

}
