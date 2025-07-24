import java.io.*;
import java.util.*;


public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int N = Integer.parseInt(br.readLine());
		
		/**
		 * 우선순위 큐 사용 (최소 힙)
		 * 
		 * - N^2개 숫자 중 가장 큰 N개의 요소만 힙에 저장
		 * - 힙에 저장된 값 중 가장 작은 값이 N번째 큰 수
		 */
		PriorityQueue<Integer> pq = new PriorityQueue<>();
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			
			for (int j = 0; j < N; j++) {
				int value = Integer.parseInt(st.nextToken());
				
				// N개까지 우선적으로 저장
				if (pq.size() < N) {
					pq.offer(value);
				}
				// 큐 최소값과 value 비교해서 큰 값을 저장
				else if (pq.peek() < value) {
					pq.poll();
					pq.offer(value);
				}
			}
		}
		
		/** 가장 큰 N개의 수 중, 가장 작은 값이 N번째로 큰 값이다 */
		System.out.println(pq.peek());
	}

}
