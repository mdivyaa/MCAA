// Armstrong numbers from 1 to 10000
public class ArmstrongNumbers {
    public static void main(String[] args) {
        for (int num = 1; num <= 10000; num++) {
            int sum = 0, temp = num, digits = String.valueOf(num).length();
            while (temp != 0) {
                int digit = temp % 10;
                sum += Math.pow(digit, digits);
                temp /= 10;
            }
            if (sum == num)
                System.out.println(num);
        }
    }
}
