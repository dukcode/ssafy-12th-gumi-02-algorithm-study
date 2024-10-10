import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.ListIterator;
import java.util.StringTokenizer;

public class B17837 {

  private static final int WHITE = 0;
  private static final int RED = 1;
  private static final int BLUE = 2;

  // 우 좌 상 하
  private static final int[] DY = {0, 0, -1, 1};
  private static final int[] DX = {1, -1, 0, 0};

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int k;
  private static int[][] board;

  private static Piece[] pieces;
  private static LinkedList<Integer>[][] status;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    k = Integer.parseInt(st.nextToken());

    board = new int[n][n];
    status = new LinkedList[n][n];
    for (int y = 0; y < n; ++y) {
      st = new StringTokenizer(br.readLine());
      for (int x = 0; x < n; ++x) {
        status[y][x] = new LinkedList<>();
        board[y][x] = Integer.parseInt(st.nextToken());
      }
    }

    pieces = new Piece[k];
    for (int idx = 0; idx < k; ++idx) {
      st = new StringTokenizer(br.readLine());
      int y = Integer.parseInt(st.nextToken()) - 1;
      int x = Integer.parseInt(st.nextToken()) - 1;
      int dir = Integer.parseInt(st.nextToken()) - 1;

      pieces[idx] = new Piece(y, x, dir);
      status[y][x].add(idx);
    }

    bw.write(String.valueOf(solve()));

    br.close();
    bw.close();
  }

  private static int solve() {

    for (int turn = 1; turn <= 1000; ++turn) {
      for (int idx = 0; idx < k; ++idx) {

        Piece piece = pieces[idx];
        int ny = piece.y + DY[piece.dir];
        int nx = piece.x + DX[piece.dir];

        if (outOfRange(ny, nx) || board[ny][nx] == BLUE) {
          piece.dir += (piece.dir % 2 == 0 ? 1 : -1);
          ny = piece.y + DY[piece.dir];
          nx = piece.x + DX[piece.dir];

          if (outOfRange(ny, nx) || board[ny][nx] == BLUE) {
            continue;
          }

        }

        int pos = getPos(piece, idx);
        int cnt = move(piece.y, piece.x, ny, nx, pos, board[ny][nx] == RED);
        if (cnt >= 4) {
          return turn;
        }
      }
    }

    return -1;
  }

  private static int move(int y, int x, int ny, int nx, int pos, boolean reverse) {
    LinkedList<Integer> indexes = status[y][x];
    ListIterator<Integer> it =
        reverse ? indexes.listIterator(indexes.size() - 1) : indexes.listIterator(pos);
    if (reverse) {
      it.next();
    }
    while (indexes.size() != pos) {
      int idx = reverse ? it.previous() : it.next();
      it.remove();
      pieces[idx].y = ny;
      pieces[idx].x = nx;
      status[ny][nx].offerLast(idx);
    }

    return status[ny][nx].size();
  }

  private static int getPos(Piece piece, int idx) {
    int n = status[piece.y][piece.x].size();
    Iterator<Integer> it = status[piece.y][piece.x].iterator();

    for (int i = 0; i < n; ++i) {
      int pos = it.next();
      if (pos == idx) {
        return i;
      }
    }

    return -1;
  }

  private static boolean outOfRange(int y, int x) {
    return y < 0 || y >= n || x < 0 || x >= n;
  }

  private static class Piece {

    int y;
    int x;
    int dir;

    public Piece(int y, int x, int dir) {
      this.y = y;
      this.x = x;
      this.dir = dir;
    }
  }


}
