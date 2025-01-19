import java.util.Scanner;

public class B30676 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String input = scanner.nextLine();

        int x = Integer.parseInt(input);

        if ((380 <= x ) & (x < 425)) {
            System.out.println("Violet");
        } else if ((425 <= x ) & (x < 450)) {
            System.out.println("Indigo");
        } else if ((450 <= x ) & (x < 495)) {
            System.out.println("Blue");
        } else if ((495 <= x ) & (x < 570)) {
            System.out.println("Green");
        } else if ((570 <= x ) & (x < 590)) {
            System.out.println("Yellow");
        } else if ((590 <= x ) & (x < 620)) {
            System.out.println("Orange");
        } else {
            System.out.println("Red");
        }
    }
}
