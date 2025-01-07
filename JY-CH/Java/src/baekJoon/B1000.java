import java.util.Scanner;

public class B1000 {
    public static void main(String[] args) {
        // 스캐너 객체 생성
        Scanner scanner = new Scanner(System.in);

        // 입력 받기
        String input = scanner.nextLine();

        // 받은 입력을 문자열 배열로 나눔
        String[] numbers = input.split(" ");

        // a,b 정수 변환
        int a = Integer.parseInt(numbers[0]);
        int b = Integer.parseInt(numbers[1]);

        // 출력
        System.out.print(a + b);
    }
}
