import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

    static int cnt = 0;
    static int N;

    public static void main(String[] args) throws Exception{
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // N 입력받기
        N = Integer.parseInt(br.readLine());

        // 백트래킹 진행
        backTracking(0, "");

        // 결과 출력
        System.out.println(cnt);
    }

    public static void backTracking(int depth, String num) {

        // 최대 깊이에 도달했을 경우
        if(depth == N) {
            // num이 3의 배수면 cnt += 1
            if((Integer.parseInt(num) % 3 == 0)) {
                cnt += 1;
            }
            return;
        }

        // 첫 번째 자리라면 1, 2만 넣기
        if(num.equals("")) {
            for(int i = 1; i < 3; i++) {
                backTracking(depth + 1, num + i);
            }
        }
        // 아니라면 0, 1, 2 넣기
        else {
            for(int i = 0; i < 3; i++) {
                backTracking(depth + 1, num + i);
            }
        }
    }
}
