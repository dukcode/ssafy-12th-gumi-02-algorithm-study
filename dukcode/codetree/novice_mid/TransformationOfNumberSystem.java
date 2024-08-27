import java.util.Scanner;

public class TransformationOfNumberSystem {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int a = sc.nextInt();
    int b = sc.nextInt();
    String n = sc.next();

    System.out.println(Integer.toString(Integer.parseInt(n, a), b));
  }

}
