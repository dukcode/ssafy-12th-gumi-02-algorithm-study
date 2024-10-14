import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class S13501 {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int t;

  private static int n;
  private static int m;
  private static int l;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    t = Integer.parseInt(br.readLine());
    for (int tc = 1; tc <= t; tc++) {
      st = new StringTokenizer(br.readLine());
      n = Integer.parseInt(st.nextToken());
      m = Integer.parseInt(st.nextToken());
      l = Integer.parseInt(st.nextToken());

      LinkedList list = new LinkedList();
      st = new StringTokenizer(br.readLine());
      for (int i = 0; i < n; i++) {
        list.addLast(Integer.parseInt(st.nextToken()));
      }

      for (int i = 0; i < m; i++) {
        st = new StringTokenizer(br.readLine());

        String command = st.nextToken();
        int idx = Integer.parseInt(st.nextToken());
        switch (command) {
          case "I":
            list.add(idx, Integer.parseInt(st.nextToken()));
            break;
          case "D":
            list.delete(idx);
            break;
          case "C":
            list.set(idx, Integer.parseInt(st.nextToken()));
            break;
          default:
            break;
        }
      }

      bw.write("#" + tc + " ");
      bw.write(String.valueOf(list.get(l)));
      bw.newLine();
    }

    br.close();
    bw.close();
  }

  private static class LinkedList {

    private Node head;
    private Node tail;
    private int size;

    public LinkedList() {
      this.head = null;
      this.tail = null;
      this.size = 0;
    }

    public void add(int idx, int value) {
      if (idx == 0) {
        addFirst(value);
        return;
      }

      if (idx == size) {
        addLast(value);
        return;
      }

      Node prev = search(idx - 1);
      Node next = prev.next;
      prev.next = new Node(value, next);
      size++;
    }

    public void addFirst(int value) {
      Node first = head;
      head = new Node(value, first);
      size++;

      if (first == null) {
        tail = head;
      }
    }

    public void addLast(int value) {
      Node last = tail;
      tail = new Node(value, null);
      size++;

      if (last == null) {
        head = tail;
      } else {
        last.next = tail;
      }
    }

    private Node search(int idx) {
      Node now = head;

      for (int i = 0; i < idx; i++) {
        now = now.next;
      }

      return now;
    }

    public int delete(int idx) {
      if (idx == 0) {
        return deleteFirst();
      }

      Node prev = search(idx - 1);
      Node toRemove = prev.next;
      prev.next = toRemove.next;
      size--;

      return toRemove.value;
    }

    public int deleteFirst() {
      Node ret = head;
      head = head.next;
      size--;

      if (head == null) {
        tail = null;
      }

      return ret.value;
    }

    public void set(int idx, int value) {
      Node node = search(idx);
      node.value = value;
    }

    public int get(int idx) {
      if (idx < 0 || idx >= size) {
        return -1;
      }

      return search(idx).value;
    }

    private static class Node {

      int value;
      Node next;

      public Node(int value, Node next) {
        this.value = value;
        this.next = next;
      }
    }
  }

}
