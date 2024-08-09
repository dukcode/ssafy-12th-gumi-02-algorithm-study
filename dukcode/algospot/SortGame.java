import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.StringTokenizer;

public class SortGame {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static Map<List<Integer>, Integer> toSort;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    toSort = new HashMap<>();
    for (int len = 1; len <= 8; ++len) {
      preCalc(len);
    }

    int c = Integer.parseInt(br.readLine());
    while (c-- > 0) {
      int n = Integer.parseInt(br.readLine());
      List<Integer> nums = new ArrayList<>();
      st = new StringTokenizer(br.readLine());
      for (int i = 0; i < n; ++i) {
        nums.add(Integer.parseInt(st.nextToken()));
      }

      nums = compressNums(nums);
      bw.write(String.valueOf(toSort.get(nums)));
      bw.newLine();
    }

    br.close();
    bw.close();
  }

  private static List<Integer> compressNums(List<Integer> nums) {

    List<Integer> ret = new ArrayList<>();
    for (int ref : nums) {
      int cnt = 0;
      for (Integer num : nums) {
        if (ref >= num) {
          cnt++;
        }
      }
      ret.add(cnt);
    }

    return ret;
  }

  private static void preCalc(int len) {
    List<Integer> arr = new ArrayList<>();
    for (int i = 1; i <= len; ++i) {
      arr.add(i);
    }

    Queue<List<Integer>> q = new LinkedList<>();
    q.offer(arr);
    toSort.put(arr, 0);

    while (!q.isEmpty()) {
      List<Integer> here = q.poll();
      int cnt = toSort.get(here);
      for (int st = 0; st <= len - 2; ++st) {
        for (int en = st + 2; en <= len; ++en) {
          List<Integer> there = reverse(here, st, en);
          if (toSort.containsKey(there)) {
            continue;
          }
          toSort.put(there, cnt + 1);
          q.offer(there);
        }
      }
    }

  }

  private static List<Integer> reverse(List<Integer> arr, int st, int en) {
    List<Integer> ret = new ArrayList<>(arr);

    while (st < --en) {
      Collections.swap(ret, st++, en);
    }

    return ret;
  }
}
