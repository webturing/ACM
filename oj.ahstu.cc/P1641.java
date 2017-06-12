import java.io.PrintWriter;
import java.util.Scanner;

public class P1641 {
    static Scanner cin = new Scanner(System.in);
    static PrintWriter cout = new PrintWriter(System.out);
    final static boolean RIGHT = true;
    final static boolean LEFT = false;
    final static int L = 100;

    static class Ant {
        boolean sick = false;

        boolean direction = RIGHT;
        int pos;

        void meet(Ant that) {
            if (this.direction == that.direction || this.pos != that.pos || this.pos < 0 || this.pos > L || that.pos < 0 || that.pos > L)
                return;
            this.direction = !this.direction;
            that.direction = !that.direction;
            if (this.sick || that.sick)
                this.sick = that.sick = true;
        }

        void move() {

            if (direction == RIGHT) {
                ++pos;

            } else {
                --pos;
            }
        }
    }

    public static void main(String[] args) {
        Ant ants[] = new Ant[cin.nextInt()];
        for (int i = 0; i < ants.length; i++) {
            ants[i] = new Ant();
            ants[i].pos = cin.nextInt();
            if (ants[i].pos < 0) {
                ants[i].direction = LEFT;
                ants[i].pos = -ants[i].pos;
            }
            ants[i].sick = false;
        }
        ants[0].sick = true;

        for (int i = 0; i <= L; i++) {
            showInfo(ants);
            for (int m = 0; m < ants.length; m++)
                ants[m].move();
            for (int j = 0; j < ants.length; j++)
                for (int k = j + 1; k < ants.length; k++)
                    ants[j].meet(ants[k]);
        }
        int tot = 0;
        for (int i = 0; i < ants.length; i++) {
            if (ants[i].sick)
                ++tot;
        }
        cout.println(tot);

        cout.close();
        cin.close();
    }

    private static void showInfo(Ant[] ants) {
        for (int i = 0; i <= L; i++) {
            for (int j = 0; j < ants.length; j++)
                if (ants[j].pos == i) {
                    if (ants[j].direction == RIGHT)
                        cout.print("Oo>");
                    else
                        cout.print("<oO");
                    if (ants[j].sick)
                        cout.print("!");
                    else
                        cout.print("@");
                } else
                    cout.print("   ");
        }
        cout.println();
    }
}
