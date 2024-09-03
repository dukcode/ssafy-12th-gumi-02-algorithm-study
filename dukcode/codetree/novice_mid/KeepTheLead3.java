import java.util.Scanner;

public class KeepTheLead3 {

    private static final int MX_TIME = 1000 * 1000;
    private static final int A = 1;
    private static final int B = 2;
    private static final int BOTH = 3;

    private static Scanner sc;

    private static int len;

    public static void main(String[] args) {
        sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();

        len = 0;
        int[] aGraph = getGraph(n);
        int[] bGraph = getGraph(m);

        int first = BOTH;
        int cnt = 0;
        for (int t = 1; t <= len; ++t) {
            int firstNow = getFirst(aGraph[t], bGraph[t]);

            if (first != firstNow) {
                first = firstNow;
                cnt++;
            }
        }

        System.out.println(cnt);

    }

    private static int getFirst(int a, int b) {
        if (a > b) {
            return A;
        }

        if (a < b) {
            return B;
        }

        return BOTH;
    }

    private static int[] getGraph(int n) {
        int[] graph = new int[MX_TIME + 1];
        int idx = 0; 
        for (int i = 0; i < n; ++i) {
            int vel = sc.nextInt();
            int time = sc.nextInt();

            while (time-- > 0) {
                graph[idx + 1] = graph[idx] + vel;
                idx++;
            }
        }

        len = Math.max(len, idx);

        return graph;
    }
}
