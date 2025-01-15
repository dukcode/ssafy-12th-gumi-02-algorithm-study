import java.util.Scanner;

public class B21300 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String[] input = scanner.nextLine().split(" ");

        int sum = 0;
        for (int i = 0; i < input.length; i++) {
            sum += Integer.parseInt(input[i]);
        }

        System.out.println(sum * 5);
    }
}
