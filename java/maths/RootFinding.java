import java.util.function.Function;

public class RootFinding {

    /**
     * Bisection method for finding the root of a function.
     * 
     * @param f       The function for which to find the root.
     * @param a       The lower bound of the interval.
     * @param b       The upper bound of the interval.
     * @param epsilon The tolerance for convergence.
     * @return The approximate root of the function.
     */
    public static double bisectionMethod(Function<Double, Double> f, double a, double b, double epsilon) {
        if (f.apply(a) * f.apply(b) >= 0) {
            throw new IllegalArgumentException("Function has the same signs at the endpoints.");
        }

        double c = a;
        while ((b - a) / 2 > epsilon) {
            c = (a + b) / 2;
            if (f.apply(c) == 0.0) {
                break;
            } else if (f.apply(c) * f.apply(a) < 0) {
                b = c;
            } else {
                a = c;
            }
        }
        return c;
    }

    /**
     * Secant method for finding the root of a function.
     * 
     * @param f       The function for which to find the root.
     * @param x0      Initial guess.
     * @param x1      Second guess.
     * @param epsilon The tolerance for convergence.
     * @return The approximate root of the function.
     */
    public static double secantMethod(Function<Double, Double> f, double x0, double x1, double epsilon) {
        double x2 = x0;
        while (Math.abs(x1 - x0) > epsilon) {
            x2 = x1 - f.apply(x1) * (x1 - x0) / (f.apply(x1) - f.apply(x0));
            x0 = x1;
            x1 = x2;
        }
        return x2;
    }

    /**
     * False Position method for finding the root of a function.
     * 
     * @param f       The function for which to find the root.
     * @param a       The lower bound of the interval.
     * @param b       The upper bound of the interval.
     * @param epsilon The tolerance for convergence.
     * @return The approximate root of the function.
     */
    public static double falsePositionMethod(Function<Double, Double> f, double a, double b, double epsilon) {
        if (f.apply(a) * f.apply(b) >= 0) {
            throw new IllegalArgumentException("Function has the same signs at the endpoints.");
        }

        double c = a; // Initialize c to a
        while (Math.abs(b - a) > epsilon) {
            c = a - f.apply(a) * (b - a) / (f.apply(b) - f.apply(a));
            if (f.apply(c) == 0.0)
                break;
            else if (f.apply(c) * f.apply(a) < 0)
                b = c;
            else
                a = c;
        }
        return c;
    }

    /**
     * Fixed Point method for finding a root of the equation x = g(x).
     * 
     * @param g            The function g(x) such that x = g(x) at the root.
     * @param initialGuess The initial guess for x.
     * @param epsilon      The tolerance for convergence.
     * @return The approximate fixed point of g.
     */
    public static double fixedPointMethod(Function<Double, Double> g, double initialGuess, double epsilon) {
        double x0 = initialGuess;
        double x1 = g.apply(x0);
        while (Math.abs(x1 - x0) > epsilon) {
            x0 = x1;
            x1 = g.apply(x0);
        }
        return x1;
    }

    // Example usage
    public static void main(String[] args) {
        // Function to find root of x^2 - 2
        Function<Double, Double> f = x -> x * x - 2;

        // Using Bisection Method
        System.out.println("Root found by Bisection Method: " + bisectionMethod(f, 0, 2, 0.001));

        // Using Secant Method
        System.out.println("Root found by Secant Method: " + secantMethod(f, 1, 2, 0.001));

        // Using False Position Method
        System.out.println("Root found by False Position Method: " + falsePositionMethod(f, 0, 2, 0.001));

        // Using Fixed Point Method
        Function<Double, Double> g = x -> Math.sqrt(2); // Example function for fixed point
        System.out.println("Root found by Fixed Point Method: " + fixedPointMethod(g, 1, 0.001));
    }
}
