import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] stack = new int[100000];
        int top = -1;

        int k = sc.nextInt();
        for (int i = 0; i < k; i++) {
            int n = sc.nextInt();
            if (n != 0) {
                stack[++top] = n;
            } else {
                top--;
            }
        }

        int ans = 0;
        while (top != -1) {
            ans += stack[top];
            top--;
        }

        System.out.println(ans);
    }
}
