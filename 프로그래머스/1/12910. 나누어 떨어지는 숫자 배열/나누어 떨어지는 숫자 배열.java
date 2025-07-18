import java.util.*;

class Solution {
    public int[] solution(int[] arr, int divisor) {
        
        List<Integer> tempResult = new ArrayList<>();
        for (int i : arr) {
            if (i % divisor == 0) {
                tempResult.add(i);
            }
        }
        
        if (tempResult.isEmpty()) {
            return new int[] {-1};
        }
        else {
            int[] result = new int[tempResult.size()];
            for (int i = 0; i < tempResult.size(); i++) {
                result[i] = tempResult.get(i);
            }
            Arrays.sort(result);
            return result;
        }
        
    }
}