import java.io.PrintWriter;
import java.util.Scanner;

public class P1604 {
    static Scanner cin = new Scanner(System.in);
    static PrintWriter cout = new PrintWriter(System.out);


    public static void main(String[] args) {
        String a = cin.next();
        String b = cin.next();
        if (a.length() != b.length())
            cout.println(1);
        else if (a.equals(b))
            cout.println(2);
        else if (a.equalsIgnoreCase(b))
            cout.println(3);
        else
            cout.println(4);
        cin.close();
        cout.close();
    }
}
