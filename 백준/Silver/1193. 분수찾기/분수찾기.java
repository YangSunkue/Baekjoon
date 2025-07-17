import java.io.*;

public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		
		int x = Integer.parseInt(br.readLine());
		
		if (x == 1) {
			System.out.println("1/1");
		}
		else if (x == 2) {
			System.out.println("1/2");
		}
		
		/** x가 3이상일 경우 진행 */
		else {
			/**
			 * 1: 우측
			 * 2: 좌측아래
			 * 3: 아래
			 * 4: 우측위
			 */
			
			/**
			 * 네비게이션
			 * 우측으로 갔으면: y+1, 좌측아래로
			 * 좌측아래로 갔으면: x+1/y-1, 좌측아래로 or 아래로
			 * 아래로 갔으면: x+1, 우측위로
			 * 우측위로 갔으면: x-1/y+1, 우측위로 or 우측으로
			 */
			int[] result = {1, 2};
			int direction = 1; // 이전 진행방향
			int cur = 2;
			while (cur < x) {
				
				// 우측으로 갔을경우 좌측아래로
				if (direction == 1) {
					result[0] += 1;
					result[1] -= 1;
					direction = 2;
				}
				// 좌측아래로 갔을경우
				else if (direction == 2) {
					// 갈수있다면 좌측아래로
					if (result[1] > 1) {
						result[0] += 1;
						result[1] -= 1;
						direction = 2;
					}
					// 아니라면 아래로
					else {
						result[0] += 1;
						direction = 3;
					}
				}
				// 아래로 갔을경우 우측위로
				else if (direction == 3) {
					result[0] -= 1;
					result[1] += 1;
					direction = 4;
				}
				// 우측위로 갔을경우
				else if (direction == 4) {
					// 갈수있다면 우측위로
					if (result[0] > 1) {
						result[0] -= 1;
						result[1] += 1;
						direction = 4;
					}
					// 아니라면 우측으로
					else {
						result[1] += 1;
						direction = 1;
					}
				}
				cur += 1;
			}
			System.out.printf("%d/%d", result[0], result[1]);
		}
	}
}
