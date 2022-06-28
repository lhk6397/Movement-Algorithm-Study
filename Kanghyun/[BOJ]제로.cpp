#include<iostream>
#include<stack>
#include<vector>
using namespace std;

int main(void) {
	int K, sum = 0;
	cin >> K;
	stack<int> stk;
	for (int i = 0; i < K; i++) {
		int tmp;
		cin >> tmp;
		if (tmp == 0)
			stk.pop();
		else
			stk.push(tmp);
	}
	int size = stk.size();
	for (int i = 0; i < size; i++) {
		sum += stk.top();
		stk.pop();
	}
	cout << sum;
}