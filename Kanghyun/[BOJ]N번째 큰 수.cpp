#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int main() {
	int T;
	cin >> T;
	int t = T;
	vector<int> ans;
	while (T > 0) {
		vector<int> numbers;
		int c = 10;
		while (c > 0) {
			int n;
			cin >> n;
			numbers.push_back(n);
			c--;
		}
		sort(numbers.rbegin(), numbers.rend());
		ans.push_back(numbers[2]);
		T--;
	}
	for (int i = 0; i < t; i++)
		cout << ans[i] << "\n";
}