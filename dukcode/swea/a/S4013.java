import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

// 특이한 자석
public class S4013 {

  private static final int NUM_GEAR = 4;
  private static final int NUM_MAGNET = 8;

  private static final int N = 0;
  private static final int S = 1;

  private static final int INITIAL = -2;
  private static final int NONE = 0;
  private static final int CW = 1;
  private static final int CCW = -1;

  private static final int TOP = 0;
  private static final int RIGHT = 2;
  private static final int LEFT = 6;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int t;

  private static int k;
  private static LinkedList<Integer>[] gears;
  private static int[][] commands;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    t = Integer.parseInt(br.readLine());

    for (int tc = 1; tc <= t; tc++) {
      input();
      bw.write("#" + tc + " ");
      bw.write(String.valueOf(solve()));
      bw.newLine();
    }

    br.close();
    bw.close();
  }

  private static int solve() {
    for (int[] command : commands) {
      int[] dirs = new int[NUM_GEAR];

      int idx = command[0];
      int dir = command[1];
      move(idx, dir, dirs);

      moveGears(dirs);
    }

    return getScore();
  }

  private static void move(int idx, int dir, int[] dirs) {
    dirs[idx] = dir;
    Arrays.fill(dirs, INITIAL);

    Queue<Integer> q = new ArrayDeque<>();

    q.offer(idx);
    dirs[idx] = dir;

    while (!q.isEmpty()) {
      int cur = q.poll();
      for (int delta : new int[]{-1, 1}) {
        int next = cur + delta;

        if (next < 0 || next >= NUM_GEAR) {
          continue;
        }

        if (dirs[next] != INITIAL) {
          continue;
        }

        int curDir = dirs[cur];

        int curMag = delta == 1 ? RIGHT : LEFT;
        int nextMag = delta == 1 ? LEFT : RIGHT;

        if (gears[cur].get(curMag) == gears[next].get(nextMag)) {
          continue;
        }

        dirs[next] = counter(curDir);
        q.offer(next);
      }
    }
  }

  private static int counter(int dir) {
    if (dir == CW) {
      return CCW;
    }

    if (dir == CCW) {
      return CW;
    }

    return NONE;
  }

  private static void moveGears(int[] dirs) {
    for (int i = 0; i < NUM_GEAR; i++) {
      LinkedList<Integer> gear = gears[i];
      if (dirs[i] == CW) {
        gear.offerFirst(gear.pollLast());
      } else if (dirs[i] == CCW) {
        gear.offerLast(gear.pollFirst());
      }
    }
  }

  private static int getScore() {
    int score = 0;
    for (int idx = 0; idx < NUM_GEAR; idx++) {
      if (gears[idx].get(TOP) == S) {
        score += (1 << idx);
      }
    }

    return score;
  }

  private static void input() throws IOException {
    k = Integer.parseInt(br.readLine());

    gears = new LinkedList[NUM_GEAR];
    for (int i = 0; i < NUM_GEAR; i++) {
      LinkedList<Integer> gear = new LinkedList<>();

      st = new StringTokenizer(br.readLine());
      for (int idx = 0; idx < NUM_MAGNET; ++idx) {
        gear.add(Integer.parseInt(st.nextToken()));
      }

      gears[i] = gear;
    }

    commands = new int[k][2];
    for (int i = 0; i < k; i++) {
      st = new StringTokenizer(br.readLine());

      int idx = Integer.parseInt(st.nextToken()) - 1;
      int dir = Integer.parseInt(st.nextToken());

      commands[i][0] = idx;
      commands[i][1] = dir;
    }
  }


}
