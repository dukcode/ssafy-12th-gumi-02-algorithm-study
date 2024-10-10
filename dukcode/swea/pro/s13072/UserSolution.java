package com.dukcode.swea.pro.s13072;

class UserSolution {

  private static final int FIRED = -1;

  private static final int MX_ID = 100_000;
  private static final int MX_TEAM = 5;
  private static final int MX_SCORE = 5;

  private int[][] soldiers; // soldiers[id] = {team, version}
  private LinkedList[][] data; // data[team][score] -> {{id, version}, ...}

  public void init() {
    soldiers = new int[MX_ID + 1][2];
    data = new LinkedList[MX_TEAM + 1][MX_SCORE + 1];
    for (int team = 1; team <= MX_TEAM; team++) {
      for (int score = 1; score <= MX_SCORE; score++) {
        data[team][score] = new LinkedList();
      }
    }
  }

  public void hire(int id, int team, int score) {
    soldiers[id][0] = team;
    soldiers[id][1] = 1;
    data[team][score].add(new Node(id, soldiers[id][1]));
  }

  public void fire(int id) {
    soldiers[id][1] = FIRED;
  }

  public void updateSoldier(int id, int score) {
    soldiers[id][1]++;
    data[soldiers[id][0]][score].add(new Node(id, soldiers[id][1]));
  }

  public void updateTeam(int team, int scoreToAdd) {
    int[] toMove = new int[MX_TEAM + 1];
    for (int from = 1; from <= MX_TEAM; ++from) {
      int to = from + scoreToAdd;
      to = Math.max(to, 1);
      to = Math.min(to, MX_TEAM);

      toMove[from] = to;
    }

    LinkedList[] res = new LinkedList[MX_TEAM + 1];
    for (int t = 1; t <= MX_TEAM; ++t) {
      res[t] = new LinkedList();
    }

    for (int from = 1; from <= MX_TEAM; ++from) {
      int to = toMove[from];
      res[to].addAll(data[team][from]);
    }

    data[team] = res;
  }

  public int bestSoldier(int team) {
    LinkedList[] scores = data[team];

    int bestId = -1;
    for (int score = MX_SCORE; score >= 1; score--) {
      Node now = scores[score].head;
      while (now != null) {
        int id = now.id;
        int version = now.version;

        now = now.next;

        if (soldiers[id][1] != version) {
          continue;
        }

        bestId = Math.max(id, bestId);
      }

      if (bestId != -1) {
        break;
      }
    }

    return bestId;
  }

  private class LinkedList {

    int size = 0;
    Node head;
    Node tail;

    public LinkedList() {
    }

    public void add(Node node) {
      if (size == 0) {
        head = node;
        tail = node;
        size++;
        return;
      }
      tail.next = node;
      tail = node;
      size++;
    }

    public void addAll(LinkedList other) {
      if (other.size == 0) {
        return;
      }

      if (size == 0) {
        head = other.head;
        tail = other.tail;
        size = other.size;
        return;
      }
      tail.next = other.head;
      tail = other.tail;
      size += other.size;
    }
  }

  private class Node {

    int id;
    int version;
    Node next;

    public Node(int id, int version) {
      this.id = id;
      this.version = version;
    }
  }
}
