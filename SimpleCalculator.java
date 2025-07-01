public class SimpleCalculator {
    public static void main(String[] args) {
        double num1 = 20;
        double num2 = 5;

        // Addition
        double sum = num1 + num2;
        System.out.println("Addition: " + num1 + " + " + num2 + " = " + sum);

        // Subtraction
        double difference = num1 - num2;
        System.out.println("Subtraction: " + num1 + " - " + num2 + " = " + difference);

        // Multiplication
        double product = num1 * num2;
        System.out.println("Multiplication: " + num1 + " * " + num2 + " = " + product);

        // Division
        if (num2 != 0) {
            double quotient = num1 / num2;
            System.out.println("Division: " + num1 + " / " + num2 + " = " + quotient);
        } else {
            System.out.println("Division by zero is not allowed.");
        }
    }
}
