import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class TheCapabilitiesOfTheDevelopmentTeam {
  private static final int MX = 987_654_321;
  private static final int N = 5;

  private static int[] arr;
  private static boolean[] taken;

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    arr = new int[N];
    for (int i = 0; i < N; ++i) {
      arr[i] = sc.nextInt();
    }

    System.out.println(solve());

    sc.close();
  }

  private static int solve() {
    taken = new boolean[N];
    List<Integer> picked = new ArrayList<>();

    int ret = solve(picked);
    return ret == MX ? -1 : ret;
  }

  private static int solve(List<Integer> picked) {
    if (picked.size() == N) {
      return getMinDiff(picked);
    }

    int ret = MX;
    for (int i = 0; i < N; ++i) {
      if (taken[i]) {
        continue;
      }

      taken[i] = true;
      picked.add(i);
      ret = Math.min(ret, solve(picked));
      picked.remove(picked.size() - 1);
      taken[i] = false;
    }

    return ret;
  }

  private static int getMinDiff(List<Integer> picked) {
    int a = arr[picked.get(0)] + arr[picked.get(1)];
    int b = arr[picked.get(2)] + arr[picked.get(3)];
    int c = arr[picked.get(4)];

    if (a == b || b == c || c == a) {
      return MX;
    }

    int ret = Math.abs(a - b);
    ret = Math.max(ret, Math.abs(b - c));
    ret = Math.max(ret, Math.abs(c - a));
    return ret;
  }
}
