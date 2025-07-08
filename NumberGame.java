import java.util.*;

public class NumberGame {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int number = (int)(Math.random() * 100) + 1;
        int guess, attempts = 0;

        do {
            System.out.print("Guess the number (1 to 100): ");
            guess = sc.nextInt();
            attempts++;
            if (guess < number)
                System.out.println("Too low!");
            else if (guess > number)
                System.out.println("Too high!");
        } while (guess != number);

        System.out.println("Correct! You guessed in " + attempts + " attempts.");
    }
}
