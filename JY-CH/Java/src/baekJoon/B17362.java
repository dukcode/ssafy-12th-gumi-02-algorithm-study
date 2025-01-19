import java.util.*;

public class B17362 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = Integer.parseInt(scanner.nextLine());

        if (n % 8 == 0 | n % 8 == 2) {
            System.out.println(2);
        } else if (n % 8 == 1) {
            System.out.println(1);
        } else if (n % 8 == 3 | n % 8 == 7) {
            System.out.println(3);
        } else if (n % 8 == 4 | n % 8 == 6) {
            System.out.println(4);
        } else {
            System.out.println(5);
        }
    }
}
