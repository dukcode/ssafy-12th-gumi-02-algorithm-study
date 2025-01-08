import java.util.Scanner;

public class B2475 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        // 생 노가다
        // 리스트 ++ 이해 후에 다시 풀것.
        String[] input = scanner.nextLine().split(" ");

        int a = Integer.parseInt(input[0]);
        int b = Integer.parseInt(input[1]);
        int c = Integer.parseInt(input[2]);
        int d = Integer.parseInt(input[3]);
        int e = Integer.parseInt(input[4]);

        System.out.println((square(a) + square(b) + square(c) + square(d) + square(e)) % 10);
    }

    public static int square(int number) {
        return number * number;
    }
}
