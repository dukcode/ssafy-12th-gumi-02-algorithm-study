import java.util.Scanner;

public class B2741 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String input = scanner.nextLine();

        int n;
        n = Integer.parseInt(input);
// for 조건문
//        for (int i = 1; i <= n; i++) {
//            System.out.println(i);
//        }

// while 반복
        int i = 1;
        while (i <= n) {
            System.out.println(i);
            i++;
        }
    }
}
