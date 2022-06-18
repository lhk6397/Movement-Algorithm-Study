#include <iostream>
#include <string>
#include<vector>
#include<sstream>
#include<algorithm>
using namespace std;

vector<int> solution(vector<string> id_list, vector<string> report, int k) {
	int list_length = id_list.size();

	sort(report.begin(), report.end());                             
	report.erase(unique(report.begin(), report.end()), report.end());     //벡터 안의 동일 원소 삭제
	int report_length = report.size();                                    //유효 신고 수

	vector<string> reported;
	for (int i = 0; i < report_length; i++) {
		stringstream ss(report[i]);
		string s1;
		while (ss >> s1)
			reported.push_back(s1);                  //reported라는 새 vector에 신고자 피신고자 나누어서 저장. 
	}                                                //짝수는 신고자 홀수는 피신고자

	vector<int> num_reporter;
	vector<int> num_respondant;
	for (int i = 0; i < report_length * 2; i++)
		for (int j = 0; j < list_length; j++)
			if (reported[i] == id_list[j])
				if (i % 2 == 0)
					num_reporter.push_back(j);                    //reported의 요소들을 숫자(번호)로 바꾸어 num_reporter 그리고 num_respondant에 저장
				else
					num_respondant.push_back(j);                 

	vector<int> answer(list_length);

	for (int i = 0; i < list_length; i++) {
		if (count(num_respondant.begin(), num_respondant.end(), i) >= k)
			for (int j = 0; j < report_length; j++)
				if (num_respondant[j] == i)
					answer[num_reporter[j]] += 1;
	}

	for (int i = 0; i < list_length; i++)
		cout << answer[i];
	return answer;
}

int main(void) {

	vector<string> report = { "ryan con", "ryan con", "ryan con", "ryan con" };
	vector<string> id_list = { "ryan", "con" };
	int k = 3;

	solution(id_list, report, k);
	

	return 0;
}