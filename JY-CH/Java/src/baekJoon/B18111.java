//import java.util.Scanner;
//
//public class B18111 {
//    public static void main(String[] args) {
//        Scanner scanner = new Scanner(System.in);
//
//        int n = scanner.nextInt();
//        int m = scanner.nextInt();
//        int b = scanner.nextInt();
//
//        int[][] field = new int[n][m];
//        int maximum = 0;
//        int minimum = 256;
//
//
//        for (int i = 0; i < n; i++) {
//            for (int j = 0; j < m; j++) {
//                field[i][j] = scanner.nextInt();
//                minimum = Math.min(minimum, field[i][j]);
//                maximum = Math.max(maximum, field[i][j]);
//            }
//        }
//
//        int answer_time = Integer.MAX_VALUE;
//        int answer_height = 0;
//
//        for (int cur = minimum; cur <= maximum; cur++) {
//            int use_time = 0;
//            int block = b;
//
//            for (int i = 0; i < n; i++) {
//                for (int j = 0; j < m; j++) {
//                    int gap = field[i][j] - cur;
//                    // 현재땅과 비교할땅차이가 양수
//                    // 지금땅이 비교할 땅보다 높음
//                    if (gap > 0) {
//                        // 차이만큼 *2로 시간을 쓴다, 파내니까
//                        use_time += gap * 2;
//                        // 파냈으면 인벤에 추가한다
//                        block += gap;
//                        // 음수
//                        // 지금땅이 비교한 땅보다 낮음.
//                    } else if (gap < 0) {
//                        // 음수라 절대값 바꾸고 돌림 너무 헷갈려서
//                        // 메꾸는건 블록을 까먹음
//                        use_time += Math.abs(gap);
//                        block -= Math.abs(gap);
//                    }
//                }
//            }
//            // block 음수면 의미 없고
//            // 소모시간이 최소가 아니면 안됨
//            if (block >= 0 && use_time <= answer_time) {
//                answer_time = use_time;
//                answer_height = cur;
//            }
//
//        }
//
//
//        System.out.println(answer_time + " " + answer_height);
//    }
//}



import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.io.IOException;
import java.util.StringTokenizer;

public class B18111 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());

        int[][] field = new int[n][m];
        int maximum = 0;
        int minimum = 256;

        // 입력 처리
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                field[i][j] = Integer.parseInt(st.nextToken());
                minimum = Math.min(minimum, field[i][j]);
                maximum = Math.max(maximum, field[i][j]);
            }
        }

        int answer_time = Integer.MAX_VALUE;
        int answer_height = 0;

        for (int cur = minimum; cur <= maximum; cur++) {
            int use_time = 0;
            int block = b;

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    int gap = field[i][j] - cur;
                    // 현재땅과 비교할땅차이가 양수
                    // 지금땅이 비교할 땅보다 높음
                    if (gap > 0) {
                        // 차이만큼 *2로 시간을 쓴다, 파내니까
                        use_time += gap * 2;
                        // 파냈으면 인벤에 추가한다
                        block += gap;
                        // 음수
                        // 지금땅이 비교한 땅보다 낮음.
                    } else if (gap < 0) {
                        // 음수라 절대값 바꾸고 돌림 너무 헷갈려서
                        // 메꾸는건 블록을 까먹음
                        use_time += Math.abs(gap);
                        block -= Math.abs(gap);
                    }
                }
            }
            // block 음수면 의미 없고
            // 소모시간이 최소가 아니면 안됨
            if (block >= 0 && use_time <= answer_time) {
                answer_time = use_time;
                answer_height = cur;
            }

        }

        bw.write(answer_time + " " + answer_height);
        br.close();
        bw.close();
    }
}