import java.util.Scanner;

public class B2739 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String input = scanner.nextLine();

        int x;
        x = Integer.parseInt(input);

        for (int i = 1; i <= 9; i++) {
            System.out.println(x + " * " + i + " = " + (x * i));
        }
    }
}
