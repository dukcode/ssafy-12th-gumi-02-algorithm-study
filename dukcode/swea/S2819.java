import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.StringTokenizer;

public class S2819 {

  private static final int[] DY = {0, 0, -1, 1};
  private static final int[] DX = {-1, 1, 0, 0};

  private static final int N = 4;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int t;

  private static int[][] board;

  private static Set<Integer> numbers;


  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    t = Integer.parseInt(br.readLine());

    for (int tc = 1; tc <= t; tc++) {
      board = new int[N][N];
      for (int y = 0; y < N; y++) {
        st = new StringTokenizer(br.readLine());
        for (int x = 0; x < N; x++) {
          board[y][x] = Integer.parseInt(st.nextToken());
        }
      }

      numbers = new HashSet<>();

      bw.write("#" + tc + " ");
      solve();
      bw.write(String.valueOf(numbers.size()));
      bw.newLine();
    }

    br.close();
    bw.close();

  }

  private static void solve() {
    List<Integer> nums = new ArrayList<>();
    for (int y = 0; y < N; y++) {
      for (int x = 0; x < N; x++) {
        nums.add(board[y][x]);
        dfs(y, x, nums);
        nums.remove(nums.size() - 1);
      }
    }
  }

  private static void dfs(int y, int x, List<Integer> nums) {
    if (nums.size() == 7) {
      int number = 0;
      for (Integer num : nums) {
        number *= 10;
        number += num;
      }

      numbers.add(number);
      return;
    }

    for (int dir = 0; dir < 4; dir++) {
      int ny = y + DY[dir];
      int nx = x + DX[dir];

      if (ny < 0 || ny >= N || nx < 0 || nx >= N) {
        continue;
      }

      nums.add(board[ny][nx]);
      dfs(ny, nx, nums);
      nums.remove(nums.size() - 1);
    }
  }
}
