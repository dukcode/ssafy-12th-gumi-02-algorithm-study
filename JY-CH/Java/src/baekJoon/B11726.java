import java.util.Scanner;

public class B11726 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String input = scanner.nextLine();

        int x = Integer.parseInt(input);
        if (x == 1) {
            System.out.println(1);
            return;
        }

        if (x == 2) {
            System.out.println(2);
            return;
        }

        int[] dp;
        dp = new int[x+1];

        dp[1] = 1;
        dp[2] = 2;
        for (int i = 3; i < x + 1; i++) {
            dp[i] = (dp[i-2] + dp[i-1]) % 10007;
        }


        System.out.println(dp[x]);
        scanner.close();
    }

}
