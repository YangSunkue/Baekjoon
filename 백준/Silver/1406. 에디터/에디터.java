import java.io.*;
import java.util.*;

public class Main {
	
	/** 연결리스트 사용 */
	static List<Character> list = new LinkedList<>();
	static ListIterator<Character> iter = list.listIterator();
	
	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer commands;
		
		/** 문자열을 연결리스트에 할당 */
		String str = br.readLine();
		for (int i = 0; i < str.length(); i++) {
			iter.add(str.charAt(i));
		}
		
		/** 명령어 개수만큼 반복 */
		int M = Integer.parseInt(br.readLine());
		for (int i = 0; i < M; i++) {
			
			commands = new StringTokenizer(br.readLine());
			modifyStr(commands);
		}
		
		/** 결과 출력 */
		StringBuilder sb = new StringBuilder();
		for (char c : list) {
			sb.append(c);
		}
		
		System.out.println(sb);
	}
	
	/** 문자열을 조작하고 현재 커서를 반환하는 함수 */
	private static void modifyStr(StringTokenizer commands) {
		
		String cmd = commands.nextToken();
		
		// 커서 왼쪽에 삽입
		if (cmd.equals("P")) {
			String value = commands.nextToken();
			iter.add(value.charAt(0));
		}
		
		// 커서를 왼쪽으로 이동
		else if (cmd.equals("L")) {
			if (iter.hasPrevious()) {
				iter.previous();
			}
		}
		
		// 커서를 오른쪽으로 이동
		else if (cmd.equals("D")) {
			if (iter.hasNext()) {
				iter.next();
			}
		}
		
		// 커서 왼쪽 문자 삭제
		else if (cmd.equals("B")) {
			if (iter.hasPrevious()) {
				iter.previous();
				iter.remove();
			}
		}
	}
}
