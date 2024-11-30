import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class B1344 {

  private static final int NUM_TIMES = 90 / 5;
  private static final int MAX_NUM_GOALS = NUM_TIMES;
  private static final int TEAM_A = 0;
  private static final int TEAM_B = 1;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static double[] probs;

  private static double[][][] cache;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    probs = new double[2];
    probs[TEAM_A] = Double.parseDouble(br.readLine()) / 100;
    probs[TEAM_B] = Double.parseDouble(br.readLine()) / 100;

    cache = new double[2][NUM_TIMES + 1][MAX_NUM_GOALS + 1];
    for (int time = 0; time <= NUM_TIMES; time++) {
      Arrays.fill(cache[TEAM_A][time], -1.0);
      Arrays.fill(cache[TEAM_B][time], -1.0);
    }

    for (int numGoals = 0; numGoals <= MAX_NUM_GOALS; numGoals++) {
      if (isPrime(numGoals)) {
        cache[TEAM_A][NUM_TIMES][numGoals] = 0.0;
        cache[TEAM_B][NUM_TIMES][numGoals] = 0.0;
      } else {
        cache[TEAM_A][NUM_TIMES][numGoals] = 1.0;
        cache[TEAM_B][NUM_TIMES][numGoals] = 1.0;
      }
    }

    bw.write(String.valueOf(
        1.0 - calcProbNotPrime(TEAM_A, 0, 0) * calcProbNotPrime(TEAM_B, 0, 0)));

    br.close();
    bw.close();

  }

  private static double calcProbNotPrime(int team, int time, int goal) {
    if (time == NUM_TIMES) {
      return cache[team][time][goal];
    }

    if (cache[team][time][goal] != -1.0) {
      return cache[team][time][goal];
    }

    double ret = 0.0;
    ret += calcProbNotPrime(team, time + 1, goal) * (1.0 - probs[team]);
    ret += calcProbNotPrime(team, time + 1, goal + 1) * (probs[team]);

    return cache[team][time][goal] = ret;
  }

  private static boolean isPrime(int n) {
    if (n <= 1) {
      return false;
    }

    for (int i = 2; i * i <= n; i++) {
      if (n % i == 0) {
        return false;
      }
    }

    return true;
  }

}
