import java.util.*;
class Main {  
  public static void main(String args[]) { 
    Scanner S = new Scanner(System.in);
    while (S.hasNext()) {
      
      String a = S.next();
      String[] v = new String[a.length()];
      for(int i=0;i<v.length;i++){
        v[i]=a.substrincrg(i, i+1);
      }
      Arrays.sort(v);
      a = "";
      for(int i=0;i<v.length;i++){
        a = a+v[i];
      }
      
      while(a.length()!=0){
        int contador = 0;
        String caracter = a.substring(0, 1);
        for(int i=0;i<v.length;i++){
          if(caracter.equals(v[i])){
            contador = contador+1;
          }
        }
        a = a.replaceAll(caracter, "");
        System.out.println(caracter+"="+contador);
      }
      System.out.println();

    } 

  } 
}