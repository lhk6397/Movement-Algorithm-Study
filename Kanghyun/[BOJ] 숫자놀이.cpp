#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
string i2s(int a);
int main() {
	
	int M, N;
	cin >> M >> N;
	vector<pair<pair<string, string>, int>> numbers;
	for (int i = M; i <= N; i++) {
		pair<pair<string, string>, int> p;
		if (i / 10 == 0){
			p.first.first = i2s(i);
			p.first.second = "a";
			p.second = i;
			numbers.push_back(p);
		}
		else {
			p.first.first = i2s(i / 10);
			p.first.second = i2s(i % 10);
			p.second = i;
			numbers.push_back(p);
		}
	}
	sort(numbers.begin(), numbers.end());
	for (int i = 0; i <= N - M; i++) {
		cout << numbers[i].second << " ";
		if (i % 10 == 9)
			cout << "\n";
	}
}
string i2s(int a) {
	string ans;
	if (a == 0)
		ans = "zero";
	if (a == 1)
		ans = "one";
	if (a == 2)
		ans = "two";
	if (a == 3)
		ans = "three";
	if (a == 4)
		ans = "four";
	if (a == 5)
		ans = "five";
	if (a == 6)
		ans = "six";
	if (a == 7)
		ans = "seven";
	if (a == 8)
		ans = "eight";
	if (a == 9)
		ans = "nine";
	return ans;
}