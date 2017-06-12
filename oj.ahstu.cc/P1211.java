import java.io.PrintWriter;
import java.util.Scanner;

public class P1211 {
    static Scanner cin = new Scanner(System.in);
    static PrintWriter cout = new PrintWriter(System.out);

    public static void main(String[] args) {
        for (int n = cin.nextInt(); n-- > 0; ) {
            String bs = Integer.toBinaryString(cin.nextInt());
            while (bs.length() < 32) bs = "0" + bs;
            cout.println(bs);
        }
        cout.close();
        cin.close();
    }
}
