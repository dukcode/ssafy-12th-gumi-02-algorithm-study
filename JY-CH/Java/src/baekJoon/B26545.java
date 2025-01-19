import java.util.*;

public class B26545 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String input = scanner.nextLine();

        int x = Integer.parseInt(input);

        int sum = 0;

        for (int i = 0; i < x; i++) {
            String newinput = scanner.nextLine();
            int number = Integer.parseInt(newinput);
            sum += number;
        }
        System.out.println(sum);
    }
}
