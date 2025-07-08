import java.util.Scanner;

public class Maximum {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter first number: ");
        int a = sc.nextInt();

        System.out.print("Enter second number: ");
        int b = sc.nextInt();

        System.out.print("Enter third number: ");
        int c = sc.nextInt();

        int max;

        // First compare a and b
        if (a > b) {
            max = a;
        } else {
            max = b;
        }

        // Then compare max with c
        if (c > max) {
            max = c;
        }

        System.out.println("The largest number is: " + max);
    }
}
