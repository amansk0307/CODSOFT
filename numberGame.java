import java.util.Scanner;
import java.util.Random;

public class numberGame {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();
        int score = 0;
        int rounds = 0;

        System.out.println("Welcome to the Guess the Number game!");

        while (true) {
            rounds++;
            System.out.println("\nRound " + rounds + ":");
            int secretNumber = random.nextInt(100) + 1;
            int attempts = 0;
            final int maxAttempts = 10;

            while (attempts < maxAttempts) {
                System.out.print("\nEnter your guess (between 1 and 100): ");
                int guess = scanner.nextInt();
                attempts++;

                if (guess == secretNumber) {
                    System.out.println("Congratulations! You've guessed the number " + secretNumber +
                            " correctly in " + attempts + " attempts!");
                    score++;
                    break;
                } else if (guess < secretNumber) {
                    System.out.println("Too low! Try again.");
                } else {
                    System.out.println("Too high! Try again.");
                }
            }

            if (attempts == maxAttempts) {
                System.out.println("\nSorry, you've run out of attempts! The correct number was " + secretNumber + ".");
            }

            System.out.println("\nYour score: " + score + "/" + rounds);
            System.out.print("\nDo you want to play again? (yes/no): ");
            String playAgain = scanner.next().toLowerCase();

            if (!playAgain.equals("yes")) {
                System.out.println("\nThanks for playing! Goodbye!");
                break;
            }
        }

        scanner.close();
    }
}
