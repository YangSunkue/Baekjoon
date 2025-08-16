import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws Exception {
		
		/**
		 * N명의 사람, 키는 1 ~ N
		 * 자기보다 큰 사람이 왼쪽에 몇명인지만 기억
		 * 
		 * 
		 * N크기 배열을 전부 0으로 초기화
		 * -> 0으로 된 부분들은, 지금 할당하려는 숫자보다 더 큰 숫자들로 채워진다.
		 * -> 즉, N[i]값만큼 0을 지나서 할당하면 끝.
		 * 1위치: N - N[i]
		 * 2위치 ~ N-1 위치: 배열 처음부터 순회하며 0이 N[i]개와 일치하면 그 다음 0인 칸에 할당
		 * N위치: 마지막 남은 0에 할당
		 */
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		/** 입력받기 */
		int N = Integer.parseInt(br.readLine());
		int[] leftPerson = new int[N];
		
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			int value = Integer.parseInt(st.nextToken());
			leftPerson[i] = value;
		}
		
		/** 결과 저장할 배열 */
		int[] result = new int[N];
		for (int i = 0; i < N; i++) {
			result[i] = 0;
		}
		
		/** 로직 */
		for (int i = 0; i < N; i++) {
			
			int jump = leftPerson[i];  // 왼쪽에 있는 키 큰 사람 수 만큼 0을 뛰어넘어야 함
			int count = 0;  // 뛰어넘은 수
			
			for (int j = 0; j < N; j++) {
				
				// 다 뛰어넘었다면 빈 자리에 배치하기
				if (count == jump && result[j] == 0) {
					result[j] = i + 1;
					break;
				}
				
				else if (result[j] == 0) {
					count++;
				}
			}
		}
		
		/** 결과 출력 */
		for (int value : result) {
			System.out.print(value + " ");
		}
	}
}
