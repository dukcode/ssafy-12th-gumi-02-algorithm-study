import java.io.BufferedReader;
import java.io.OutputStreamWriter;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.util.StringTokenizer;

public class B10808 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int[] alphabet = new int[26];

        String word = br.readLine();

        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            alphabet[c - 'a']++;
        }

        for (int i = 0; i < 26; i++) {
            bw.write(alphabet[i] + " ");
        }
        br.close();
        bw.close();
    }
}
