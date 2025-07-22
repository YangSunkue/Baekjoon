import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		/**
		 * 가장 작은 창고 면적 구하기
		 * 한번 내려가면 다시 올라오면 안된다
		 * 
		 * 올라가기: 기존 높이로 쭉 가다가, 높은 걸 만날때마다 올라간다
		 * 내려가기: 가장 높은 곳에 도달했다면 내려갈 준비를 한다
		 *     1. 남은 기둥 중 가장 높은 높이로 내려간 후 해당 기둥까지 진행한다
		 *     2. 남은 기둥이 없다면 종료한다.
		 */
		
		int N = Integer.parseInt(br.readLine());
		
		/** 기둥들 입력받기 */
		int[][] columns = new int[N][2];
		for (int i = 0; i < N; i++) {
			
			st = new StringTokenizer(br.readLine());
			int location;
			int height;
			
			location = Integer.parseInt(st.nextToken());
			height = Integer.parseInt(st.nextToken());
			
			columns[i] = new int[] {location, height, i};
		}
		Arrays.sort(columns, (a, b) -> a[0] - b[0]);  // 위치 순서대로 기둥 정렬
		
		if (N == 1) {
			System.out.println(columns[0][1]);
		}
		
		/**
		 * 올라갈때: 기둥높이 * 다음기둥까지의 거리 = 면적
		 * 최고점 왔을때: 현재기둥높이 더하기, 내려가기 로직으로 전환
		 * 내려갈때: 다음기둥 없으면 그대로 종료, 있으면 다음기둥높이 * 다음기둥까지의 거리
		 */
		else {
			
			int[] highestColumn = findHighestColumn(columns, 0);
			int result = 0;  // 총 면적
			int[] prev = columns[0];
			
			/** 올라갈 때 */
			for (int i = 1; i < N; i++) {
				
				// 최고 높이 기둥 만났을 경우, 내려가기 로직으로 전환
				if (columns[i][0] == highestColumn[0]) {
					result += prev[1] * (columns[i][0] - prev[0]);
					result += columns[i][1];
//					System.out.printf("%d -> 내려가기 전환\n", result);
					break;
				}
				
				// 올라갈 때 높은 기둥 만났을 경우
				else if (columns[i][1] >= prev[1]) {
					result += prev[1] * (columns[i][0] - prev[0]);
					prev = new int[] {columns[i][0], columns[i][1], i};
//					System.out.println(result);
				}
			}
			
			/** 내려갈 때 */
			prev = highestColumn;
			int[] nextColumn = findHighestColumn(columns, prev[2] + 1);
//			System.out.printf("find함수 인자 prev %d %d %d\n", prev[0], prev[1], prev[2] + 1);
//			System.out.printf("내려가기 로직 시작 nextColumn: %d %d", nextColumn[0], nextColumn[1]);
			while (nextColumn != null) {
				
				result += nextColumn[1] * (nextColumn[0] - prev[0]);
				prev = nextColumn;
				nextColumn = findHighestColumn(columns, prev[2] + 1);  // 다음 기둥이 존재하면 계속 내려가기
				
//				System.out.printf("내려가는 로직 - %d\n", result);
			}
			
			System.out.println(result);
			
		}
		
	}
	
	/** 지정된 인덱스부터 끝까지 탐색하여, 가장 높은 기둥 정보(위치, 높이)를 리턴하는 함수 */
	private static int[] findHighestColumn(int[][] arr, int idx) {
		
		/** 남은 기둥이 없다면 null 리턴 */
		if (idx >= arr.length) {
			return null;
		}
		
		// 위치, 높이, 인덱스
		int highestColumn[] = new int[] {0, 0, 0};
		for (int i = idx; i < arr.length; i++) {
			
			if (arr[i][1] >= highestColumn[1]) {
				highestColumn[0] = arr[i][0];
				highestColumn[1] = arr[i][1];
				highestColumn[2] = i;
			}
		}
		return highestColumn;
		
	}

}
