import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		st = new StringTokenizer(br.readLine());
		
		int[] origin = {1, 1, 2, 2, 2, 8};
		int[] result = new int[6];
		for(int i = 0; i < 6; i++) {
			
			int value = Integer.parseInt(st.nextToken());
			result[i] = origin[i] - value;
		}
		
		for(int i = 0; i < result.length; i++) {
			System.out.printf("%d ", result[i]);
		}
	}
}
