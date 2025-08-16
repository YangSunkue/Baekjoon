import java.io.*;
import java.util.*;

public class Main {
	
	static ArrayDeque<int[]> queue = new ArrayDeque<>();
	static int[][] result;
	static int N;
	static int M;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		
		/**
		 * 0: 벽
		 * 1: 땅
		 * 2: 목표지점
		 * 각 지점에서 목표지점까지 가는 최단거리 출력
		 * 
		 * BFS
		 * 목표지점부터 값을 1씩 늘려가며 4방향 뻗어나가기
		 * 
		 * 벽은 0 출력
		 * 갈 수 없는 땅은 -1출력
		 * 
		 * BFS 후 result 배열
		 * 0: 목표지점
		 * 자연수: 간 땅들
		 * 나머지 0: 못간 땅들
		 * -2: 벽들
		 * 
		 * 출력값으로 변환하기
		 * 1. 목표지점 제외한 0을 -1로 만들기
		 * 2. 벽들을 0으로 만들기
		 */
		
		/** 입력받기 */
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		int[][] table = new int[N][M];
		
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			
			for (int j = 0; j < M; j++) {
				table[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		/** 결과 2차원 배열 제작 */
		int sx = -9999;
		int sy = -9999;
		result = new int[N][M];
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				
				if (table[i][j] == 2) {  // 시작 좌표 구해두기 (목표지점)
					sx = i;
					sy = j;
				}
				
				// 벽은 -2로 저장
				if (table[i][j] == 0) {
					result[i][j] = -2;
				}
				// 나머지는 전부 0으로 저장
				else {
					result[i][j] = 0;
				}
			}
		}
		
		int[] dx = new int[] {-1, 1, 0, 0};
		int[] dy = new int[] {0, 0, -1, 1};
		
		/** BFS */
		queue.offer(new int[] {sx, sy, result[sx][sy]});  // 시작좌표, 시작값(0) 넣기
		while (!queue.isEmpty()) {
			
			int[] prev = queue.poll();
			int px = prev[0];
			int py = prev[1];
			int pValue = prev[2];
			
			// 4방향 진행
			for (int i = 0; i < 4; i++) {
				int nx = px + dx[i];
				int ny = py + dy[i];
				
				if (canGo(nx, ny)) {
					result[nx][ny] = pValue + 1;
					queue.offer(new int[] {nx, ny, pValue + 1});
					
				}
			}
		}
		
		/** 출력에 맞는 형태로 바꾸기 */
		// 1. 못 간 땅을 -1로 바꾸기
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (result[i][j] == 0) {
					result[i][j] = -1;
				}
			}
		}
		
		// 2. 벽을 0으로 바꾸기
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (result[i][j] == -2) {
					result[i][j] = 0;
				}
			}
		}
		
		// 3. 시작지점을 0으로 바꾸기
		result[sx][sy] = 0;
		
		/** 결과 출력 */
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				sb.append(result[i][j]).append(" ");
			}
			sb.append("\n");
		}
		System.out.println(sb);
		
	}
	
	/** 해당 좌표에 진행할 수 있는지 판단하는 함수 */
	private static boolean canGo(int nx, int ny) {
		// N*M 범위 안에 있고, 시작지점이 아니고, 아직 간 적 없는 땅이라면 갈 수 있다
		if (0 <= nx && nx < N && 0 <= ny && ny < M && result[nx][ny] == 0) {
			return true;
		}
		return false;
	}
}
//3 3
//2 0 1
//1 0 0
//1 1 1
