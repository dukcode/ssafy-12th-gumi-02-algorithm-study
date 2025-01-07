import java.util.Scanner;

public class B1330 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String input = scanner.nextLine();

        String[] numbers = input.split(" ");

        int a = Integer.parseInt(numbers[0]);
        int b = Integer.parseInt(numbers[1]);

        if (a > b) {
            System.out.print(">");
        }
        else if (a == b) {
            System.out.print("==");
        }
        else {
            System.out.print("<");
        }

    }
}
