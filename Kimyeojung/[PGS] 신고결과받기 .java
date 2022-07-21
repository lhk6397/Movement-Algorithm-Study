import java.util.*;

class 신고결과받기 {
    
	public int[] solution(String[] id_list, String[] report, int k) {
		int[] answer=new int[id_list.length];
		
		Map <String, Set<String>> report_info=new HashMap<>();
		Map <String, Integer> answer_info=new HashMap<>();
		
		for(int i=0; i<id_list.length; i++) {
			Set <String> singo=new HashSet<>();
			report_info.put(id_list[i], singo);
			answer_info.put(id_list[i], 0);
		}
		
		for(String a:report) {
			String[] str=a.split(" ");
			String sin=str[0];
			String go=str[1];
			report_info.get(go).add(sin);
		}
		
		for(String b:report_info.keySet()) {
			Set <String> go1=report_info.get(b);
			if(go1.size()>=k) {
				for(String id:go1) {
					answer_info.put(id, answer_info.get(id)+1);
				}
			}
		}
		
		for(int i=0; i<id_list.length; i++) {
			answer[i]=answer_info.get(id_list[i]);
		}
		
		return answer;
	}

}
