import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// N : 포켓몬 종류
// P : 포켓몬
// M : P에 대한 총 사탕 개수
// K : P를 진화시키기 위해 필요한 사탕 개수
// 진화시킬 수 있는 총 마릿수 , 가장 많이 진화시킨 포켓몬 출력
// 총 마릿수가 동일할 경우 일찍 나타는 애 출력하면 됨. max < 마릿수
// 진화시키면 사탕 2개 추가로 줌

public class Main {
    public static void main(String[] args) throws Exception{
        
        // 입력받기///////////////
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        String monster[] = new String[N];
        int KM[][] = new int[N][2];

        for(int i = 0; i < N; i++) {
            monster[i] = br.readLine();

            st = new StringTokenizer(br.readLine());
            KM[i][0] = Integer.parseInt(st.nextToken());
            KM[i][1] = Integer.parseInt(st.nextToken());
        }
        // 입력받기///////////////

        // 진화횟수
        int upgrade = 0;
        // 포켓몬별 진화횟수 담을 변수
        int maxCount = Integer.MIN_VALUE;
        // 최대진화 포켓몬 저장할 변수
        String maxMonster = "";

        // 포켓몬별로 반복하기
        for(int i = 0; i < N; i++) {
            int candy = KM[i][1];
            int count = 0;

            // 진화에 필요한 사탕보다 가진 사탕이 많으면 진행
            while(true) {
                if(candy >= KM[i][0]) {
                    candy -= KM[i][0] - 2;
                    upgrade += 1;
                    count += 1;
                }
                else {
                    break;
                }
            }
            // 이 포켓몬이 최대 진화횟수라면 maxMonster 갱신
            if(count > maxCount) {
                maxCount = count;
                maxMonster = monster[i];
            }
        }
        System.out.println(upgrade);
        System.out.println(maxMonster);
    }
}