import java.io.*;
import java.util.*;


public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int N = Integer.parseInt(br.readLine());
		int[] table = new int[N*N];
		
		/** 숫자를 하나의 배열로 전부 입력받기 */
		int idx = 0;
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			
			for (int j = 0; j < N; j++) {
				table[idx] = Integer.parseInt(st.nextToken());
				idx++;
			}
		}
		Arrays.sort(table);  // 오름차순 정렬
		
		/** N번째로 큰 수 출력 */
		System.out.println(table[table.length - N]);
	}

}
