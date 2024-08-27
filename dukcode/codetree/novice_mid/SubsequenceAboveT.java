import java.util.Scanner;

public class SubsequenceAboveT {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int n = sc.nextInt();
    int t = sc.nextInt();

    int ans = 0;
    int lastLength = 0;
    for (int i = 0; i < n; ++i) {
      int num = sc.nextInt();

      if (num > t) {
        lastLength++;
      } else {
        lastLength = 0;
      }

      ans = Math.max(ans, lastLength);
    }

    System.out.println(ans);
  }

}
