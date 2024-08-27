import java.util.PriorityQueue;
import java.util.Scanner;

public class LineUpStudents2 {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int n = sc.nextInt();

    PriorityQueue<Student> students = new PriorityQueue<>(
        (a, b) -> a.h == b.h ? b.w - a.w : a.h - b.h);
    for (int i = 0; i < n; i++) {
      int h = sc.nextInt();
      int w = sc.nextInt();
      int idx = i + 1;

      Student student = new Student(h, w, idx);
      students.add(student);
    }

    while (!students.isEmpty()) {
      System.out.println(students.poll());
    }

  }

  private static class Student {

    final int h;
    final int w;

    private final int idx;

    public Student(int h, int w, int idx) {
      this.h = h;
      this.w = w;
      this.idx = idx;
    }

    @Override
    public String toString() {
      return h + " " + w + " " + idx;
    }
  }

}
