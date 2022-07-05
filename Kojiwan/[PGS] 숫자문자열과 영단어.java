import java.util.*;
class Solution {

	String[] english_num = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
	
    public int solution(String s) {
        int answer = 0;
        String s_answer = "";
        
        for(int i = 0; i<s.length(); ++i) {
        	char tmp = s.charAt(i);
        	if(!Character.isDigit(tmp)) {
        		String substr = s.substring(i, i + 2);
        		String ans="";
        		for(int j = 0; j< english_num.length; ++j) {
        			if(english_num[j].contains(substr)) {
        				ans = english_num[j];
        				s_answer += j;
        			}
        		}
        		i += (ans.length() - 1);
        	}
        	else { s_answer += tmp; }
        }
        answer = Integer.parseInt(s_answer);
        return answer;
    }
}