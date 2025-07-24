class Solution {
    public String solution(String s) {
        
        String[] str = s.split("");
        String result = "";
        int len = str.length;
        
        if (len % 2 == 1) {
            result += str[len / 2];
        }
        else {
            result += str[len / 2 - 1];
            result += str[len / 2];
        }
        
        return result;
    }
}