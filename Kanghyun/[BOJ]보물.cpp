#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int main() {
	int N, S = 0;
	vector<int> A, B;
	cin >> N;
	for (int i = 0; i < N; i++) {
		int tmp;
		cin >> tmp;
		A.push_back(tmp);
	}
	for (int i = 0; i < N; i++) {
		int tmp;
		cin >> tmp;
		B.push_back(tmp);
	}
	sort(A.begin(), A.end());
	sort(B.rbegin(), B.rend());
	for (int i = 0; i < N; i++) {
		int tmp = A[i] * B[i];
		S += tmp;
	}
	cout << S;
}