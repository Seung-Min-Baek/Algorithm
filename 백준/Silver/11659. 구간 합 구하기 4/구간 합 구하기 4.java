
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		int[] arr1 = new int[n];
		st= new StringTokenizer(br.readLine());
		
		int[] arr = new int[n+1];
		
		for (int i = 1; i <= n; i++) 
			arr[i] = arr[i-1] + Integer.parseInt(st.nextToken());
		
		for (int j = 0; j < m; j++) {
			st= new StringTokenizer(br.readLine());
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());
			
			
			
			System.out.println(arr[y]- arr[x-1]);
			
		}
		
	}
}
