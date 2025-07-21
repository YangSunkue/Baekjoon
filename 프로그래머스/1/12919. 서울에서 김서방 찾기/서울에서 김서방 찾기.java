class Solution {
    public String solution(String[] seoul) {
        
        String location = findKim(seoul);
        return "김서방은 " + location + "에 있다";
    }
    
    
    
    private static String findKim(String[] arr) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i].equals("Kim")) {
                return String.valueOf(i);
            }
        }
        return "-1";
    }
}