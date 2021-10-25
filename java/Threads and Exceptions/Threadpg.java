import java.util.Random;
public class Threadpg
{
    public static void main(String[] args)
    {
        Rand r=new Rand();
        r.start();
        sn s1=new sn(3);
        s1.start();
        cn c1=new cn(2);
        c1.start();
    }      
}
class Rand extends Thread
{
    public void run()
    {
        Random ra=new Random();
        int i=0;
        while(i<10)
        {
            System.out.println(ra.nextInt(100)+"");
            i++;
        }
    }
}
class sn extends Thread
{
    int n;
    public sn(int n)
    {
        this.n=n;
    }
    public void run()
    {
        System.out.println("Square of number is:"+Math.pow(n,2));
    }
}
class cn extends Thread
{
    int n;
    public cn(int n)
    {
        this.n=n;
    }
    public void run()
    {
        System.out.println("Cube of number is:"+Math.pow(n,3));
    }
}
