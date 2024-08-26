import java.util.Scanner;

public class TheDayOfTheDay {

  private static int toDayOfWeek(String dayOfWeek) {
    switch (dayOfWeek) {
      case "Mon":
        return 0;
      case "Tue":
        return 1;
      case "Wed":
        return 2;
      case "Thu":
        return 3;
      case "Fri":
        return 4;
      case "Sat":
        return 5;
      case "Sun":
        return 6;
      default:
        return -1;
    }
  }

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    Date from = new Date(sc.nextInt(), sc.nextInt());
    Date to = new Date(sc.nextInt(), sc.nextInt());
    String dayOfWeek = sc.next();

    from = from.plus(toDayOfWeek(dayOfWeek));
    int cnt = 0;
    while (from.before(to)) {
      cnt++;
      from = from.plus(7);
    }

    System.out.println(cnt);
  }

  private static class Date {

    private static final int[] daysOfWeek = {0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

    private final int month;
    private final int day;

    public Date(int month, int day) {
      this.month = month;
      this.day = day;
    }

    public boolean before(Date date) {
      if (this.month == date.month) {
        return this.day <= date.day;
      }

      return this.month <= date.month;
    }

    public Date plus(int days) {
      int nextMonth = month + (day + days) / daysOfWeek[month];
      int nextDay = (day + days) % daysOfWeek[month];

      return new Date(nextMonth, nextDay);
    }
  }

}
