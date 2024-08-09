import java.util.Arrays;
import java.util.Random;

public class Treap {

  public static void main(String[] args) {
    int[] cnt = new int[10 + 1];
    for (int i = 0; i < 5000; ++i) {
      Node root = new Node(10);
      for (int num = 1; num <= 10; ++num) {
        root = insert(root, new Node(num));
      }

      int leftSize = root.left == null ? 0 : root.left.size;
      int rightSize = root.right == null ? 0 : root.right.size;

      cnt[Math.abs(leftSize - rightSize)]++;
    }

    System.out.println(Arrays.toString(cnt));
  }

  public static Node insert(Node root, Node node) {
    if (root == null) {
      return node;
    }

    if (root.priority < node.priority) {
      Node[] splitted = split(root, node.key);
      node.setLeft(splitted[0]);
      node.setRight(splitted[1]);
      return node;
    } else if (root.key > node.key) {
      root.setLeft(insert(root.left, node));
    } else {
      root.setRight(insert(root.right, node));
    }
    return root;
  }

  // split 두 개의 트립으로 분리한다.
  private static Node[] split(Node root, int key) {
    Node[] pair = new Node[2];
    if (root == null) {
      return pair;
    }

    // 루트가 key 미만이면 오른쪽 서브트리를 쪼갠다.
    if (root.key < key) {
      Node[] rs = split(root.right, key);
      root.setRight(rs[0]);
      return new Node[]{root, rs[1]};
    } else { // root가 key 이상이면 왼쪽 서브트리를 쪼갠다.
      Node[] ls = split(root.left, key);
      root.setLeft(ls[1]);
      return new Node[]{ls[0], root};
    }
  }

  public static Node erase(Node root, int key) {
    if (root == null) {
      return root;
    }
    if (root.key == key) {
      Node ret = merge(root.left, root.right);
      root = null;
      return ret;
    }

    if (root.key > key) {
      root.setLeft(erase(root.left, key));
    } else {
      root.setRight(erase(root.right, key));
    }
    return root;
  }

  // a와 b가 두 개의 트립이고, max(a) < min(b)일 때 이 둘을 합친다.
  private static Node merge(Node a, Node b) {
    if (a == null) {
      return b;
    }
    if (b == null) {
      return a;
    }

    if (a.priority < b.priority) {
      b.setLeft(merge(a, b.left));
      return b;
    }
    a.setRight(merge(a.right, b));
    return a;
  }

  public static int countLessThan(Node root, int x) {
    if (root == null) {
      return 0;
    }

    if (root.key >= x) {
      return countLessThan(root.left, x);
    }

    // x가 현재 노드보다 클 경우
    // 왼쪽 서브트리 크기 + 현재 노드 + 오른쪽에서 x보다 작은 노드 수
    int ls = root.left == null ? 0 : root.left.size;
    return ls + 1 + countLessThan(root.right, x);
  }

  public static Node kth(Node root, int k) {
    // 왼쪽 서브트리의 크기를 우선 계산한다.
    int leftSize = 0;
    if (root.left != null) {
      leftSize = root.left.size;
    }

    if (k < leftSize) {
      return kth(root.left, k);
    }

    if (k == leftSize) {
      return root;
    }

    return kth(root.right, k - leftSize - 1);
  }

  public static class Node {

    int key;
    int priority;
    int size;
    Node left, right;

    // data, left, right 초기화 및 난수 우선순위 생성
    Node(int key) {
      this.key = key;
      this.priority = new Random().nextInt();
      this.left = this.right = null;
    }

    private void setLeft(Node left) {
      this.left = left;
      calcSize();
    }

    private void setRight(Node right) {
      this.right = right;
      calcSize();
    }

    private void calcSize() {
      size = 1;
      if (left != null) {
        size += left.size;
      }
      if (right != null) {
        size += right.size;
      }
    }

    public String toString() {
      return String.valueOf(key);
    }
  }
}
