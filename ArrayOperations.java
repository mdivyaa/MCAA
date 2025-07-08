import java.util.*;

public class ArrayOperations {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Ask the user for array length
        System.out.print("Enter the size of the array: ");
        int n = sc.nextInt();

        int[] arr = new int[n];

        // Read array elements
        System.out.println("Enter " + n + " elements:");
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        // A. Find largest and smallest
        int max = arr[0], min = arr[0], sum = 0;

        for (int num : arr) {
            if (num > max) max = num;
            if (num < min) min = num;
            sum += num;
        }

        // B. Calculate average
        double avg = (double) sum / n;

        // C. Remove duplicates using LinkedHashSet
        Set<Integer> unique = new LinkedHashSet<>();
        for (int num : arr) {
            unique.add(num);
        }

        // Print results
        System.out.println("\nOriginal Array: " + Arrays.toString(arr));
        System.out.println("Maximum: " + max);
        System.out.println("Minimum: " + min);
        System.out.println("Total: " + sum);
        System.out.println("Average: " + avg);
        System.out.println("Array without duplicates: " + unique);
    }
}
