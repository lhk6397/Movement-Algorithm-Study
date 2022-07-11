#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int main() {
	pair<int, pair<int, int>> stats;
	vector<pair<int, pair<int, int>>> contestants;
	int N;
	cin >> N;
	for (int i = 0; i < N; i++) {
		int region, idn, score;
		cin >> region >> idn >> score;
		pair<int, pair<int, int>> s;
		s.first = score;
		s.second.first = region;
		s.second.second = idn;
		contestants.push_back(s);
	}
	sort(contestants.rbegin(), contestants.rend());
	int c = contestants.size();
	if (contestants[0].second.first == contestants[1].second.first)
		for (int i = 2; i < c; i++) {
			if (contestants[1].second.first == contestants[i].second.first)
				continue;
			else {
				cout << contestants[0].second.first << " " << contestants[0].second.second << "\n";
				cout << contestants[1].second.first << " " << contestants[1].second.second << "\n";
				cout << contestants[i].second.first << " " << contestants[i].second.second << "\n";
				break;
			}
		}
	else {
		cout << contestants[0].second.first << " " << contestants[0].second.second << "\n";
		cout << contestants[1].second.first << " " << contestants[1].second.second << "\n";
		cout << contestants[2].second.first << " " << contestants[2].second.second << "\n";
	}
}