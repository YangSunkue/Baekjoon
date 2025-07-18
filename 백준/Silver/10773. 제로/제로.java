import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int K = Integer.parseInt(br.readLine());
		
		Deque<Integer> stack = new ArrayDeque<>();
		for (int i = 0; i < K; i++) {
			
			int value = Integer.parseInt(br.readLine());
			if (value != 0) {
				stack.push(value);
			}
			else {
				stack.pop();
			}
		}
		
		System.out.println(getStackSum(stack));
	}
	
	private static int getStackSum(Deque<Integer> stack) {
		
		if (stack.isEmpty()) {
			return 0;
		}
		
		int result = 0;
		while (!stack.isEmpty()) {
			result += stack.pop();
		}
		
		return result;
	}

}
