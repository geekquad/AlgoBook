import java.util.Scanner;
public class Excep
{
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        System.out.print("Enter a :-");
        int a = in.nextInt();
        System.out.print("Enter b:-");
        int b = in.nextInt();
        Compute compute = new Compute(a, b); //creating constructors to assign values(pass parameters to the class fields)
        compute.compute_a_by_b(); //instance variable to call a method
    }
}
class Compute
{
    private int a,b;
    public Compute(int m, int n)
    {
        a = m; //assigning values to the class fields
        b = n;
    }
    public void compute_a_by_b()
    {
        try
        {
            if (b != 0)
            {
                System.out.println("Result a/b="+(float)1.0*a/b);
            }
            else throw new ArithmeticException("Denominator is 0! Division by zero ERROR");
        }
        catch (ArithmeticException e)
        {
            System.out.println("Error !!!!: " + e);
        }
    }
}