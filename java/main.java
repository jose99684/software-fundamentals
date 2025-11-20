// import static org.junit.jupiter.api.Assertions.assertEquals;

// import org.junit.jupiter.api.Test;

public class Main {
  public static void main(String[] args) {
    //1. Define vars and/or constants
    float num1=10, num2=3, add=0, subs=0, mult=0, div=0;
    
    //2. Initialize vars and/or const
    num1 = 10;
    num2 = 3;
    add = 0;
    subs = 0;
    mult = 0;
    div = 0;
    
    //3. Processes
    add = num1 + num2;
    subs = num1 - num2;
    mult = num1 * num2;
    div = num1 / num2;

    //4. Outputs
    System.out.println("Addition: "+ add);
    System.out.println("Substraction: "+ subs);
    System.out.println("Multiplication: "+ mult);
    System.out.println("Division: "+ div);
  }

  // @Test
  // void addition() {
  //     assertEquals(2, 1 + 1);
  // }
}