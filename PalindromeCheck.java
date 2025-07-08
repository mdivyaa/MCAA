import java.util.Scanner;

public class PalindromeCheck {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a word or number: ");
        String input = sc.nextLine();

        // Convert input to lowercase for case-insensitive comparison
        input = input.toLowerCase();

        boolean isPalindrome = true;

        for (int i = 0; i < input.length() / 2; i++) {
            if (input.charAt(i) != input.charAt(input.length() - 1 - i)) {
                isPalindrome = false;
                break;
            }
        }

        if (isPalindrome)
            System.out.println("It is a Palindrome");
        else
            System.out.println("It is Not a Palindrome");
    }
}
