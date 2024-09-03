import java.util.*;
import java.io.*;

public class AddAllTheNumbersOnThePath {

    private static final int[] dy = {-1, 0, 1, 0};
    private static final int[] dx = {0, 1, 0, -1};

    private static BufferedReader br;
    private static BufferedWriter bw;
    private static StringTokenizer st;

    private static int n;
    private static int t;
    private static char[] commands;
    private static int[][] board;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter(new OutputStreamWriter(System.out));

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        t = Integer.parseInt(st.nextToken());

        commands = br.readLine().toCharArray();

        board = new int[n][n];
        for (int y = 0; y < n; ++y) {
            st = new StringTokenizer(br.readLine());
            for (int x = 0; x < n; ++x) {
                board[y][x] = Integer.parseInt(st.nextToken());
            }
        }
        


        bw.write(String.valueOf(getScore()));
        bw.newLine();

        br.close();
        bw.close();
    }

    private static int getScore() {
        int y = n / 2;
        int x = n / 2;
        int dir = 0;

        int ret = board[y][x];
        for (char command : commands) {
            switch (command) {
                case 'F':
                    int ny = y + dy[dir];
                    int nx = x + dx[dir];

                    if (ny < 0 || ny >= n || nx < 0 || nx >= n) {
                        continue;
                    }

                    y = ny;
                    x = nx;
                    ret += board[y][x];
                    break;

                case 'L':
                    dir = (dir + 3) % 4;
                    break;

                case 'R':
                    dir = (dir + 1) % 4;
                    break;

                default:
                    break;
            }
        }

        return ret;
    }
}