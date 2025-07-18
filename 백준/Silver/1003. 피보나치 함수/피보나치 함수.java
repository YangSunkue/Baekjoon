import java.io.*;

public class Main {
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		/**
		 * [ [현재숫자, 0호출횟수, 1호출횟수] ... ]
		 * [ [0, 1, 0], [1, 0, 1], [1, 1, 1] ... ]
		 */
		int[][] fiboTable = new int[41][3];
		fiboTable[0] = new int[] {0, 1, 0};
		fiboTable[1] = new int[] {1, 0, 1};
		
		for (int i = 2; i < fiboTable.length; i++) {
			fiboTable[i] = new int[] {
					fiboTable[i-1][0] + fiboTable[i-2][0],
					fiboTable[i-1][1] + fiboTable[i-2][1],
					fiboTable[i-1][2] + fiboTable[i-2][2]
			};
		}
		
		int T = Integer.parseInt(br.readLine());
		for (int i = 0; i < T; i++) {
			
			int value = Integer.parseInt(br.readLine());
			System.out.printf("%d %d\n", fiboTable[value][1], fiboTable[value][2]);
		}
	}
}
