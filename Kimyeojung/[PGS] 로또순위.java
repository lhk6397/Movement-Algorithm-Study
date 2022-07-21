import java.util.Arrays;

class Solution {
	
	public int[] solution(int[] lottos, int[] win_nums) {
		
		int[] answer = {0,0};
		int zero=0;
		
		Arrays.sort(lottos);
		Arrays.sort(win_nums);
		
		for(int i=0;i<6;i++) {
			if(lottos[i]==0)
				zero++;
		}
		
		for(int i=0;i<6;i++) {
				for(int j=zero;j<6;j++) {
					if(win_nums[i]==lottos[j]) {
						answer[0]++;
						answer[1]++;
					}
				}
		}
		
		answer[0]+=zero;
		
		for(int i=0;i<2;i++) {
			if(answer[i]==6) answer[i]=1;
			else if(answer[i]==5) answer[i]=2;
			else if(answer[i]==4) answer[i]=3;
			else if(answer[i]==3) answer[i]=4;
			else if(answer[i]==2) answer[i]=5;
			else answer[i]=6;
		}
		
		return answer;
	}
}
