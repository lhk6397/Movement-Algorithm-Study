#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int main() {
	int T, classno = 1;
	cin >> T;
	int t = T;
	vector<int> ans;
	while (T > 0) {
		ans.push_back(classno);
		classno++;
		int n, i = 0, score;
		vector<int> scores;
		vector<int> diffs;
		cin >> n;
		while (i < n) {
			cin >> score;
			scores.push_back(score);
			i++;
		}
		sort(scores.begin(),scores.end());
		ans.push_back(scores[n - 1]);
		ans.push_back(scores[0]);
		i = 0;
		while (i < n - 1) {
			diffs.push_back(scores[i + 1] - scores[i]);
			i++;
		}
		sort(diffs.rbegin(), diffs.rend());
		ans.push_back(diffs[0]);
		T--;
	}
	for (int i = 0; i < t; i++) {
		cout << "Class " << ans[4 * i] << "\n";
		cout << "Max " << ans[4 * i + 1] << ", Min " << ans[4 * i + 2] << ", Largest gap " << ans[4 * i + 3] << "\n";
	}
}