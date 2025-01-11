import java.util.Scanner;

public class B28235 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String input = scanner.nextLine();

        // 조건문
//        if (input.equals("SONGDO")) {
//            System.out.print("HIGHSCHOOL");
//        } else if (input.equals("CODE")) {
//            System.out.print("MASTER");
//        } else if (input.equals("2023")) {
//            System.out.print("0611");
//        } else {
//            System.out.print("CONTEST");
//        }

        // switch문
        switch (input) {
            case "SONGDO" -> System.out.print("HIGHSCHOOL");
            case "CODE" -> System.out.print("MASTER");
            case "2023" -> System.out.print("0611");
            default -> System.out.print("CONTEST");
        }
    }
}
