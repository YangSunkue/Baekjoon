import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int[] numbers = new int[5];
		int sumOfNumbers = 0;
		for (int i = 0; i < 5; i++) {
			
			int curValue = Integer.parseInt(br.readLine());
			
			numbers[i] = curValue;
			sumOfNumbers += curValue;
		}
		Arrays.sort(numbers);
		
		System.out.println(getAverage(sumOfNumbers));
		System.out.println(numbers[2]);
	}
	
	private static int getAverage(int sum) {
		return sum / 5;
	}
}