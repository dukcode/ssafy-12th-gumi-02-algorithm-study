package com.dukcode.swea.a;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Objects;
import java.util.Set;
import java.util.StringTokenizer;

// 원자 소멸 시뮬레이션
public class S5648 {

  private static final int SIZE = 1000;

  // 상 하 좌 우
  private static final int[] DX = {0, 0, -1, 1};
  private static final int[] DY = {1, -1, 0, 0};

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int t;

  private static int n;
  private static List<Atom> atoms;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    t = Integer.parseInt(br.readLine());
    for (int tc = 1; tc <= t; tc++) {
      n = Integer.parseInt(br.readLine());

      atoms = new ArrayList<>();
      for (int i = 0; i < n; i++) {
        int[] atom = new int[4];

        st = new StringTokenizer(br.readLine());
        int x = Integer.parseInt(st.nextToken()) * 2; // x
        int y = Integer.parseInt(st.nextToken()) * 2; // y
        int dir = Integer.parseInt(st.nextToken()); // dir
        int e = Integer.parseInt(st.nextToken()); // e

        atoms.add(new Atom(x, y, dir, e));
      }

      bw.write("#" + tc + " ");
      bw.write(String.valueOf(solve()));
      bw.newLine();
    }

    br.close();
    bw.close();
  }

  private static int solve() {

    int ret = 0;
    while (!atoms.isEmpty()) {
      for (int i = atoms.size() - 1; i >= 0; --i) {
        Atom atom = atoms.get(i);

        atom.move();

        if (!atom.inRange()) {
          atoms.remove(i);
        }
      }

      Set<Point> points = new HashSet<>();
      Set<Point> toDelete = new HashSet<>();
      for (Atom atom : atoms) {
        Point point = atom.toPoint();
        if (points.contains(point)) {
          toDelete.add(point);
        } else {
          points.add(point);
        }
      }

      for (int i = atoms.size() - 1; i >= 0; --i) {
        Atom atom = atoms.get(i);
        Point point = atom.toPoint();
        if (toDelete.contains(point)) {
          ret += atom.e;
          atoms.remove(i);
        }
      }

    }

    return ret;
  }

  private static class Point {

    int x;
    int y;

    public Point(int x, int y) {
      this.x = x;
      this.y = y;
    }

    @Override
    public boolean equals(Object o) {
      if (this == o) {
        return true;
      }
      if (o == null || getClass() != o.getClass()) {
        return false;
      }
      Point point = (Point) o;
      return x == point.x && y == point.y;
    }

    @Override
    public int hashCode() {
      return Objects.hash(x, y);
    }
  }

  private static class Atom {

    int x;
    int y;
    int dir;
    int e;

    public Atom(int x, int y, int dir, int e) {
      this.x = x;
      this.y = y;
      this.dir = dir;
      this.e = e;
    }

    public boolean inRange() {
      return -SIZE * 2 <= x && x <= SIZE * 2 && -SIZE * 2 <= y && y <= SIZE * 2;
    }

    public void move() {
      x += DX[dir];
      y += DY[dir];
    }

    public Point toPoint() {
      return new Point(x, y);
    }

  }

}
