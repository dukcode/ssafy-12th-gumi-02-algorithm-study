import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Scanner;

public class GetMedian2 {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int n = sc.nextInt();

    PriorityQueue<Integer> lowerQ = new PriorityQueue<>(Comparator.reverseOrder());
    PriorityQueue<Integer> upperQ = new PriorityQueue<>();

    for (int i = 0; i < n; ++i) {
      if (lowerQ.size() == upperQ.size()) {
        lowerQ.add(sc.nextInt());
      } else {
        upperQ.add(sc.nextInt());
      }

      if (!lowerQ.isEmpty() && !upperQ.isEmpty() &&
          lowerQ.peek() > upperQ.peek()) {
        int a = lowerQ.poll();
        int b = upperQ.poll();
        upperQ.add(a);
        lowerQ.add(b);
      }

      if (i % 2 == 0) {
        System.out.print(lowerQ.peek() + " ");
      }

    }
  }
}
