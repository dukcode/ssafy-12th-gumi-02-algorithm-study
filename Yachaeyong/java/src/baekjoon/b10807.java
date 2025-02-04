package baekjoon;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class b10807 {

  public static void main(String[] args) throws IOException {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    int N = Integer.parseInt(br.readLine());
    int[] arr = new int[N];
    int count = 0;

    StringTokenizer st = new StringTokenizer(br.readLine());

    for (int i = 0; i < N; i++) {
      arr[i] = Integer.parseInt(st.nextToken());
    }

    int v = Integer.parseInt(br.readLine());

//    for (int i = 0; i < arr.length; i++) {
//      if (v == arr[i]) {
//        count++;
//      }
//    }
    for (int j : arr) {
      if (j == v) {
        count ++;
      }
    }
    System.out.println(count);

    br.close();
    bw.close();
  }
}