import java.util.Scanner;

public class VowelConsonant {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a string: ");
        String input = sc.nextLine().toLowerCase(); // Convert to lowercase

        String vowels = "aeiou";
        int vowelCount = 0, consonantCount = 0;

        for (int i = 0; i < input.length(); i++) {
            char ch = input.charAt(i);

            if (Character.isLetter(ch)) {
                if (vowels.indexOf(ch) != -1) {
                    System.out.println(ch + " : Vowel");
                    vowelCount++;
                } else {
                    System.out.println(ch + " : Consonant");
                    consonantCount++;
                }
            }
        }

        System.out.println("\nTotal Vowels: " + vowelCount);
        System.out.println("Total Consonants: " + consonantCount);
    }
}
