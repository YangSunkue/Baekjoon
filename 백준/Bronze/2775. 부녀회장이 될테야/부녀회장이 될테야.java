import java.io.*;

public class Main {
	
	/** 14*14 모든 집에 각 몇 명이 있는지 미리 계산 */
	static int[][] house = new int[15][14];  // 0층 ~ 14층 -> 총 15개 층, 14개 호
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		/** 0층 미리 초기화 */
		for (int i = 1; i < 15; i++) {
			house[0][i-1] = i;
		}
		
		/** 모든 호실의 사람 수 계산 */
		for (int i = 1; i < 15; i++) {
			for (int j = 0; j < 14; j++) {
				
				house[i][j] = getPopulation(i, j);
			}
		}
		
		/** 메인 로직 */
		int T = Integer.parseInt(br.readLine());
		for (int i = 0; i < T; i++) {
			int x = Integer.parseInt(br.readLine());
			int y = Integer.parseInt(br.readLine());
			
			System.out.println(house[x][y-1]);
		}
	}
	
	/**
	 * 층과 호실을 입력받아 몇 명의 사람이 있는지 계산합니다.
	 */
	private static int getPopulation(int x, int y) {
		
		int population = 0;
		for (int i = 0; i < y+1; i++) {
			population += house[x-1][i];
		}
		
		return population;
	}
}
