import java.io.*;
import java.util.*;

public class Main {
    static int N, M;
    static char[][] maps;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        
        maps = new char[N][M];
        for (int i = 0; i < N; i++) {
            maps[i] = br.readLine().toCharArray();
        }
        
        int result = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (maps[i][j] == 'L') {
                    result = Math.max(result, bfs(i, j));
                }
            }
        }
        
        System.out.println(result);
    }

    static boolean goingNoGoing(int nx, int ny, int[][] visited) {
        return nx >= 0 && nx < N && ny >= 0 && ny < M && maps[nx][ny] == 'L' && visited[nx][ny] == 0;
    }

    static int bfs(int i, int j) {
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{i, j});
        
        int[][] visited = new int[N][M];
        visited[i][j] = 1;
        
        int count = 0;
        
        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int x = current[0];
            int y = current[1];
            
            for (int k = 0; k < 4; k++) {
                int nx = x + dx[k];
                int ny = y + dy[k];
                
                if (goingNoGoing(nx, ny, visited)) {
                    visited[nx][ny] = visited[x][y] + 1;
                    count = Math.max(count, visited[nx][ny]);
                    queue.add(new int[]{nx, ny});
                }
            }
        }
        
        return count - 1;
    }
}