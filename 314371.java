import java.util.*;
class Main {  
  public static void main(String args[]) { 
    Scanner S = new Scanner(System.in);
    int A = 1;
    int B = 1;
    int n = S.nextInt();
    double x1 = 0;
    double x2 = 0;

    for(int i=1;i<=n;i++){
      long C = S.nextLong();
      C = C*-2;
      double det = Math.pow(B, 2)-(4*A*C);

      if( det < 0){
        System.out.println("Better Luck Next Time");
      }
      else{
        x1 = (-B+Math.sqrt(det))/(2*A);
        x2 = (-B-Math.sqrt(det))/(2*A);
      }
   
      if(x1==(int)(x1)){
        System.out.println("Go On Bob "+(int)(x1));
      }
      else 
      {if (x2 == (int)(x2)){
        System.out.println("Go On Bob "+(int)(x2));
      }
      else{
        System.out.println("Better Luck Next Time");
      }
      }
    }

  } 
}