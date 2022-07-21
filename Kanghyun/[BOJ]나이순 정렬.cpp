#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;
int main() {
	int N, n, no = 1;
	cin >> N;
	n = N;
	vector<pair<int, pair<int, string>>> ans;
	while (n > 0) {
		int age;
		string name;
		pair<int, pair<int, string>> person;
		cin >> age >> name;
		person.first = age;
		person.second.first = no;
		person.second.second = name;
		ans.push_back(person);
		no++;
		n--;
	}
	sort(ans.begin(), ans.end());
	for (int i = 0; i < N; i++)
		cout << ans[i].first << " " << ans[i].second.second << "\n";
}