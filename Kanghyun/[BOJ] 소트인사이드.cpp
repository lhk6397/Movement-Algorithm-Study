#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int main() {
	int N, divider = 1;
	cin >> N;
		vector<int> num;
		for (int i = 0; i < 10; i++) {
			if (N / divider == 0)
				break;
			num.push_back((N / divider) % 10);
			divider *= 10;
		}
		sort(num.begin(), num.end(), greater<>());
		for (int i = 0; i < num.size(); i++)
			cout << num[i];
}