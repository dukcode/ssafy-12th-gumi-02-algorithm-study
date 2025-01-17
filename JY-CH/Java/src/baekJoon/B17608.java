import java.util.*;

public class B17608 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = Integer.parseInt(scanner.nextLine());

        int[] stickset = new int[n];
        for (int i = 0; i < n; i++) {
            int stick = Integer.parseInt(scanner.nextLine());
            stickset[i] = stick;
        }

        int cnt = 1;
        int cur_stick = stickset[n-1];
        for (int i = 0; i < n; i++) {

            if (cur_stick < stickset[(n-1)-i]) {
                cnt += 1;
                cur_stick = stickset[(n-1)-i];
            }
        }

        System.out.println(cnt);
    }
}
