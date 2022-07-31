#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int main() {
	int M, N;
	vector<int> set, one;
	cin >> N >> M;
	for (int i = 0; i < M; i++) {
		int s, o;
		cin >> s >> o;
		set.push_back(s); one.push_back(o);
	}
	sort(set.begin(), set.end());
	sort(one.begin(), one.end());
	int all_one, set_one, all_set;
	all_one = one[0] * N;
	set_one = set[0] * (N / 6) + one[0] * (N % 6);
	if (N % 6 == 0)
		all_set = set[0] * (N / 6);
	else
		all_set = set[0] * (N / 6 + 1);
	int tmp;
	tmp = min(all_one, set_one);
	cout << min(tmp, all_set);
}