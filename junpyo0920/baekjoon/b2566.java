import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[][] matrix = new int[9][9];
        for (int i = 0; i < 9; i++) {
            String[] strInput = sc.nextLine().split(" ");
            for (int j = 0; j < 9; j++) {
                matrix[i][j] = Integer.parseInt(strInput[j]);
            }
        }

        int maxVal = 0;
        int[] pos = {0, 0};
        for (int y = 0; y < 9; y++) {
            for (int x = 0; x < 9; x++) {
                if (matrix[y][x] >= maxVal) {
                    maxVal = matrix[y][x];
                    pos[0] = y + 1;
                    pos[1] = x + 1;
                }
            }
        }

        System.out.println(maxVal);
        System.out.println(pos[0] + " " + pos[1]);
    }
}
