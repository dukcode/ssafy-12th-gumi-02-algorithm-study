import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

/**
 * 암호문3
 */
public class S1230 {

  private static final int T = 10;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    for (int tc = 1; tc <= T; tc++) {
      LinkedList ll = new LinkedList();

      int n = Integer.parseInt(br.readLine());

      int[] initArr = new int[n];
      st = new StringTokenizer(br.readLine());
      for (int i = 0; i < n; ++i) {
        initArr[i] = Integer.parseInt(st.nextToken());
      }

      ll.extend(0, initArr);

      int m = Integer.parseInt(br.readLine());
      st = new StringTokenizer(br.readLine());
      for (int i = 0; i < m; ++i) {
        char cmd = st.nextToken().charAt(0);

        int x;
        int y;
        switch (cmd) {
          case 'I':
            x = Integer.parseInt(st.nextToken());
            y = Integer.parseInt(st.nextToken());

            int[] addArr = new int[y];
            for (int j = 0; j < y; ++j) {
              addArr[j] = Integer.parseInt(st.nextToken());
            }

            ll.extend(x, addArr);
            break;
          case 'D':
            x = Integer.parseInt(st.nextToken());
            y = Integer.parseInt(st.nextToken());

            ll.delete(x, y);
            break;
          case 'A':
            y = Integer.parseInt(st.nextToken());
            for (int j = 0; j < y; ++j) {
              ll.add(Integer.parseInt(st.nextToken()));
            }
            break;
          default:
            break;
        }
      }

      bw.write(String.format("#%d %s", tc, ll));
      bw.newLine();
    }

    br.close();
    bw.close();
  }

  private static class LinkedList {

    private Node head;
    private Node tail;

    public LinkedList() {
    }

    private Node getNewNode(int data) {
      return new Node(data);
    }

    public void extend(int idx, int[] nums) {
      int st = 0;
      if (idx == 0) {
        if (head != null) {
          Node newNode = getNewNode(nums[0]);
          newNode.next = head;
          head = newNode;
        } else {
          head = getNewNode(nums[0]);
        }

        idx = 1;
        st = 1;
      }

      Node cur = head;
      for (int i = 1; i < idx; ++i) {
        cur = cur.next;
      }

      for (int i = st; i < nums.length; ++i) {
        Node newNode = getNewNode(nums[i]);
        newNode.next = cur.next;
        cur.next = newNode;
        cur = newNode;
      }

      if (cur.next == null) {
        tail = cur;
      }
    }

    public void delete(int idx, int cnt) {
      Node cur = head;
      if (idx == 0) {
        for (int i = 0; i < cnt; ++i) {
          cur = cur.next;
        }

        head = cur;
        return;
      }

      for (int i = 1; i < idx; ++i) {
        cur = cur.next;
      }

      Node anchor = cur.next;
      for (int i = 0; i < cnt; ++i) {
        cur = cur.next;
      }

      anchor.next = cur.next;
      if (anchor.next == null) {
        tail = anchor;
      }
    }

    public void add(int data) {
      Node cur = tail;
      Node newNode = getNewNode(data);

      if (cur == null) {
        head = tail = newNode;
        return;
      }

      cur.next = newNode;
      tail = newNode;
    }

    @Override
    public String toString() {
      StringBuilder sb = new StringBuilder();
      Node cur = head;

      int cnt = 10;
      while (cnt-- > 0) {
        sb.append(String.format("%d ", cur.data));
        cur = cur.next;
      }

      return sb.toString();
    }

    private static class Node {

      private final int data;
      private Node next;

      public Node(int data) {
        this.data = data;
        this.next = null;
      }
    }
  }

}
