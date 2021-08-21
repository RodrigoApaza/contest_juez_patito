import java.util.*;
class Main {
  public static void main(String[] args) {
    Scanner S = new Scanner(System.in);
    try{ 
      while(true){
        int n = S.nextInt();
      
    
        int[] v = new int[n];
        for(int i=0;i<n;i++){
          v[i] = S.nextInt();
        }
        int mayor = v[0];

        for(int i=0;i<n;i++){
          if(v[i]>mayor){
            mayor = v[i];
          }
        }
        System.out.println(mayor);
      }
    
    }
    catch(NoSuchElementException a){

    }
    

  }
}