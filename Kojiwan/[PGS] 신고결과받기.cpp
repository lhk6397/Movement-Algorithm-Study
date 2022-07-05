#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

vector<int> solution(vector<string> id_list, vector<string> report, int k) {
	vector<int> answer(id_list.size(), 0);
	sort(report.begin(), report.end());
	report.erase(unique(report.begin(), report.end()), report.end());
	map<string, vector<string>> reported_list;

	for (int i = 0; i < report.size(); ++i) {
		size_t pos = report[i].find(' ');
		string reporter = report[i].substr(0, pos); // muzi
		string reported = report[i].substr(pos + 1, report[i].size() - 1); // frodo
		reported_list[reported].push_back(reporter);
	}

	for (auto iter = reported_list.begin(); iter != reported_list.end(); ++iter) {
		if (iter->second.size() < k) continue;
		for (size_t i = 0; i < iter->second.size(); ++i) {
			auto it = find(id_list.begin(), id_list.end(), iter->second[i]) - id_list.begin();
			++answer[it];
		}
	}

	for (int i = 0; i < id_list.size(); ++i) {
		cout << answer[i] << ' ';
	}


	return answer;
}