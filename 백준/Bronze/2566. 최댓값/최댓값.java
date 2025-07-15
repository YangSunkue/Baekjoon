import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws Exception {
		
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int result = 0;
		int xValue = 0;
		int yValue = 0;
		for (int i = 0; i < 9; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < 9; j++) {
				
				int curValue = Integer.parseInt(st.nextToken());
				if (result <= curValue) {
					result = curValue;
					xValue = i + 1;
					yValue = j + 1;
				}
			}
		}
		System.out.printf("%d\n", result);
		System.out.printf("%d %d", xValue, yValue);
	}
}