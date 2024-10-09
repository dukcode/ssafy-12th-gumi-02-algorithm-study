import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Objects;
import java.util.Set;
import java.util.StringTokenizer;

// 최대 상금
public class S1244 {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int t;
  private static char[] cards;
  private static int cnt;

  private static int maxPrice;
  private static Set<Status> visited;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    t = Integer.parseInt(br.readLine());
    for (int c = 1; c <= t; c++) {
      st = new StringTokenizer(br.readLine());
      cards = st.nextToken().toCharArray();
      cnt = Integer.parseInt(st.nextToken());

      visited = new HashSet<>();
      maxPrice = 0;

      visited.add(new Status(cnt, cards));
      solve(cnt);

      bw.write("#" + c + " ");
      bw.write(String.valueOf(maxPrice));
      bw.newLine();
    }

    br.close();
    bw.close();

  }

  private static void solve(int cnt) {
    if (cnt == 0) {
      maxPrice = Math.max(maxPrice, Integer.parseInt(String.valueOf(cards)));
      return;
    }

    for (int i = 0; i < cards.length; i++) {
      for (int j = i + 1; j < cards.length; j++) {
        swap(i, j);
        if (!visited.contains(new Status(cnt, cards))) {
          visited.add(new Status(cnt, cards));
          solve(cnt - 1);
        }
        swap(i, j);
      }
    }

  }

  private static void swap(int a, int b) {
    char temp = cards[a];
    cards[a] = cards[b];
    cards[b] = temp;
  }

  private static class Status {

    int cnt;
    char[] cards;

    public Status(int cnt, char[] cards) {
      this.cnt = cnt;
      this.cards = new char[cards.length];
      System.arraycopy(cards, 0, this.cards, 0, cards.length);
    }

    @Override
    public boolean equals(Object o) {
      if (this == o) {
        return true;
      }
      if (o == null || getClass() != o.getClass()) {
        return false;
      }
      Status status = (Status) o;
      return cnt == status.cnt && Objects.deepEquals(cards, status.cards);
    }

    @Override
    public int hashCode() {
      return Objects.hash(cnt, Arrays.hashCode(cards));
    }
  }
}
