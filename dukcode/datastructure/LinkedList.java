import java.util.NoSuchElementException;
import java.util.StringJoiner;

public class LinkedList<E> {

  private Node<E> head;
  private Node<E> tail;
  private int size;

  public LinkedList() {
    this.head = null;
    this.tail = null;
    this.size = 0;
  }

  public void addFirst(E data) {
    Node<E> first = head;
    head = new Node<>(data, first);
    size++;

    if (first == null) {
      tail = head;
    }
  }

  public void addLast(E data) {
    Node<E> last = tail;
    tail = new Node<>(data, null);
    size++;

    if (last == null) {
      head = tail;
    } else {
      last.next = tail;
    }
  }

  private Node<E> search(int index) {
    Node<E> now = head;
    for (int i = 0; i < index; i++) {
      now = now.next;
    }

    return now;
  }

  public void add(int index, E data) {
    if (index < 0 || index > size) {
      throw new IndexOutOfBoundsException();
    }

    if (index == 0) {
      addFirst(data);
      return;
    }

    if (index == size) {
      addLast(data);
      return;
    }

    Node<E> prev = search(index - 1);
    Node<E> next = prev.next;

    prev.next = new Node<>(data, next);
    size++;
  }

  public void set(int index, E value) {
    if (index < 0 || index >= size) {
      throw new IndexOutOfBoundsException();
    }

    Node<E> node = search(index);
    node.data = value;
  }

  @Override
  public String toString() {
    if (head == null) {
      return "[]";
    }

    StringJoiner sj = new StringJoiner(", ", "[", "]");

    Node<E> now = head;
    while (now != null) {
      sj.add(String.valueOf(now.data));
      now = now.next;
    }

    return sj.toString();
  }

  public E get(int index) {
    if (index < 0 || index >= size) {
      throw new IndexOutOfBoundsException();
    }

    return search(index).data;
  }

  public E removeFirst() {
    if (head == null) {
      throw new NoSuchElementException();
    }

    Node<E> ret = head;
    head = head.next;
    size--;

    if (head == null) {
      tail = null;
    }

    return ret.data;
  }

  public E remove(int index) {
    if (index < 0 || index >= size) {
      throw new IndexOutOfBoundsException();
    }

    if (index == 0) {
      return removeFirst();
    }

    Node<E> prev = search(index - 1);
    Node<E> toRemove = prev.next;

    prev.next = toRemove.next;
    size--;

    return toRemove.data;
  }

  public E removeLast() {
    return remove(size - 1);
  }

  private static class Node<E> {

    E data;
    Node<E> next;

    public Node(E data, Node<E> next) {
      this.data = data;
      this.next = next;
    }
  }
}
