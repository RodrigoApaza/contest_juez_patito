import java.util.*;
class Main {
  public static void main(String[] args) {
    Scanner S = new Scanner(System.in);
    try{ 
      while(true){
        int n = S.nextInt();
        int[] v = new int[n];
        for(int i=0;i<n;i++){
          v[i]= S.nextInt();
        }
        int valor = S.nextInt();
        int numMonedas = 0;
        for(int j=n-1;j>=0;j--){
          numMonedas = numMonedas + (valor/v[j]);
          valor = valor - ((valor/v[j])* v[j]);
        
        }
        if (valor ==0){
          System.out.println(numMonedas);
        }
        else{
          System.out.println(-1);
        }
    
        
      }
    
    }
    catch(NoSuchElementException a){

    }
    

  }
}