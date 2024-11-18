import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();
        int[][] arr = new int[N][N];
        int temp=0;
        for(int i=0;i<N;i++)
        {
            for(int j=0;j<N;j++)
            {
                arr[i][j]=in.nextInt();
            }
        }
        for(int i=0;i<N;i++)
        {
            for(int j=0;j<N/2;j++)
            {
                temp=arr[i][j];
                arr[i][j]=arr[i][N-j-1];
                arr[i][N-j-1]=temp;
                
            }
        }
        for(int i=0;i<N;i++)
        {
            for(int j=0;j<N;j++)
            {
                System.out.print(arr[i][j]+ " ");
                
            }
            System.out.println(" ");
        }
        
        
    }
}
