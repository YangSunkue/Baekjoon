import java.io.*;
import java.util.*;

public class Main {

    static int N; // 테스트 케이스 개수
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static char[][] tower;
    static int[][] visited;
    static int w, h;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine()); // 테스트 케이스 개수

        // 테스트 케이스 개수만큼 반복
        for(int i = 0; i < N; i++) {

            // 입력받기
            StringTokenizer st = new StringTokenizer(br.readLine());
            w = Integer.parseInt(st.nextToken());
            h = Integer.parseInt(st.nextToken());

            tower = new char[h][w];
            visited = new int[h][w];

            for(int j = 0; j < h; j++) {
                String line = br.readLine();
                for(int k = 0; k < w; k++) {
                    tower[j][k] = line.charAt(k);
                    visited[j][k] = -1;
                }
            }

            // BFS 진행하고 결과 출력
            System.out.println(fire());
        }
    }

    // 진행할지 말지 알려주는 함수
    public static boolean goingNoGoing(int nx, int ny, char who) {

        // 불일 경우
        if(who == '*') {
            // tower 안에 있고 빈 공간 또는 상근이 시작 위치일때 True
            if(0 <= nx && nx < h && 0 <= ny && ny < w && (tower[nx][ny] == '.' || tower[nx][ny] == '@')) {
                return true;
            }
            return false;
        }

        // 상근이일 경우
        else {
            // tower 안에 있고 아직 안 간 빈 공간일때 true
            if(0 <= nx && nx < h && 0 <= ny && ny < w && visited[nx][ny] == -1 && tower[nx][ny] == '.') {
                return true;
            }
            return false;
        }
    }

    // bfs 메인 로직
    public static String fire() {

        // 큐 사용
        Queue<int[]> queue = new LinkedList<>();
        int start[] = new int[2];

        // 불이 먼저 진행되어야 하므로 먼저 큐에 넣는다
        for(int i = 0; i < h; i++) {
            for(int j = 0; j < w; j++) {

                // 불일 경우 큐에 삽입
                if(tower[i][j] == '*') {
                    queue.add(new int[]{i, j, '*'});
                }

                // 상근이 시작 위치 저장만 해두기 ( 지도에 @는 하나뿐이다 )
                if(tower[i][j] == '@') {
                    start[0] = i;
                    start[1] = j;
                }
            }
        }

        // 상근이 시작 위치 큐에 삽입 + visited 처리
        queue.add(new int[]{start[0], start[1], '.'});
        visited[start[0]][start[1]] = 0;

        // bfs 시작
        while(!queue.isEmpty()) {

            // 큐에서 좌표 꺼내기
            int[] here = queue.poll();
            int x = here[0];
            int y = here[1];
            char who = (char)here[2];

            // 탈출 조건 ( 상근이가 4방향 중 어느 한쪽 끝에 도달했다면 )
            if(who == '.' && (x == 0 || x == h-1 || y == 0 || y == w-1)) {

                // 거리를 String 형태로 return한다
                return String.valueOf(visited[x][y] + 1);
            }

            // 4방향 진행
            for(int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                // 진행할 수 있을 때
                if(goingNoGoing(nx, ny, who)) {

                    // 불이라면 진행시키고 큐에 넣기
                    if(who == '*') {
                        tower[nx][ny] = '*';
                        queue.add(new int[]{nx, ny, '*'});
                    }

                    // 상근이라면 visited 거리 갱신하고 큐에 넣기
                    else {
                        visited[nx][ny] = visited[x][y] + 1;
                        queue.add(new int[]{nx, ny, '.'});
                    }
                }
            }
        }
        return "IMPOSSIBLE";
        
    }
}