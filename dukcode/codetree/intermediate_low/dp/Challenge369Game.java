package com.dukcode.codetree.intermediate_low.dp;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Challenge369Game {

  public static final int MOD = 1000000007;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static long[] pt = new long[100005];
  private static long[][] dp = new long[100005][5];
  private static long ans;
  private static boolean is_suc;
  private static int sm;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    // 문자열 a와 그 길이 n을 입력받습니다.
    String a = br.readLine();
    n = a.length();

    // 10의 거듭제곱을 미리 계산합니다.
    pt[0] = 1;
    for (int i = 1; i <= n; i++) {
      pt[i] = pt[i - 1] * 10 % MOD;
    }

    // 각 숫자에 대해 동적 프로그래밍을 수행합니다.
    // dp[i][j] :: 앞 i번째 자릿수까지 봤을 때, 각 자릿수의 합이 3의 배수이며, 자릿수 중 3, 6, 9가 나타나지 않았으며,
    // 이 뒤에 0 ~ 9 중 어느 숫자를 붙여도 되는 형태의 자릿수의 개수
    for (int i = 0; i < n; i++) {
      int num = a.charAt(i) - '0';
      for (int x = 0; x < 10; x++) {
        // 3, 6, 9인 경우 별도로 처리합니다.
        if (x == 3 || x == 6 || x == 9) {
          ans += (dp[i][0] + dp[i][1] + dp[i][2]) * pt[n - i - 1] % MOD;
          ans %= MOD;
          continue;
        }

        // 나머지 숫자들에 대한 dp 계산을 수행합니다.
        for (int k = 0; k < 3; k++) {
          dp[i + 1][(x + k) % 3] += dp[i][k];
          dp[i + 1][(x + k) % 3] %= MOD;
        }
      }

      // 현재 숫자가 num보다 작은 경우를 처리합니다.
      for (int x = 0; x < num; x++) {
        if (is_suc || x == 3 || x == 6 || x == 9) {
          ans += pt[n - i - 1];
          ans %= MOD;
        } else {
          dp[i + 1][(x + sm) % 3]++;
          dp[i + 1][(x + sm) % 3] %= MOD;
        }
      }

      // 현재 숫자가 3, 6, 9인 경우 플래그를 설정합니다.
      if (num == 3 || num == 6 || num == 9) {
        is_suc = true;
      } else {
        sm += num;
      }
    }

    // 마지막 자릿수를 처리합니다.
    if (is_suc) {
      ans++;
      ans %= MOD;
    } else {
      dp[n][sm % 3]++;
      dp[n][sm % 3] %= MOD;
    }

    // 최종 결과를 계산하여 출력합니다.
    ans += dp[n][0];
    ans += (MOD - 1);
    ans %= MOD;

    bw.write(String.valueOf(ans));

    br.close();
    bw.close();

  }
}
