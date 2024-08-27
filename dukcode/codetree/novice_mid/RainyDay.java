import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class RainyDay {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int n = sc.nextInt();

    List<Information> infos = new ArrayList<>();
    for (int i = 0; i < n; ++i) {
      String date = sc.next();
      String dayOfWeek = sc.next();
      String weather = sc.next();

      if (!weather.equals("Rain")) {
        continue;
      }

      infos.add(new Information(date, dayOfWeek, weather));
    }

    Collections.sort(infos);

    System.out.println(infos.get(0));
  }

  private static class Information implements Comparable<Information> {

    private int y;
    private int m;
    private int d;
    private String dayOfWeek;
    private String weather;

    public Information(String date, String dayOfWeek, String weather) {
      String[] tokens = date.split("-");
      this.y = Integer.parseInt(tokens[0]);
      this.m = Integer.parseInt(tokens[1]);
      this.d = Integer.parseInt(tokens[2]);
      this.dayOfWeek = dayOfWeek;
      this.weather = weather;
    }

    @Override
    public String toString() {
      return String.format("%02d-%02d-%02d %s %s", y, m, d, dayOfWeek, weather);
    }

    @Override
    public int compareTo(Information o) {
      if (this.y == o.y && this.m == o.m) {
        return this.d - o.d;
      }

      if (this.y == o.y) {
        return this.m - o.m;
      }

      return this.y - o.y;
    }
  }

}
