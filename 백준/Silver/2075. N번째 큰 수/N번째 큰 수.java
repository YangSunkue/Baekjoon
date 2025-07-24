import java.io.*;
import java.util.*;


public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int N = Integer.parseInt(br.readLine());
		
		/** 우선순위 큐 사용 */
		PriorityQueue<Integer> maxPq = new PriorityQueue<>(Collections.reverseOrder());
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			
			for (int j = 0; j < N; j++) {
				int value = Integer.parseInt(st.nextToken());
				maxPq.offer(value);
			}
		}
		
		/** N번째 큰 수 추출 */
		int result = -1;
		for (int i = 0; i < N; i++) {
			result = maxPq.poll();
		}
		
		System.out.println(result);
	}

}
