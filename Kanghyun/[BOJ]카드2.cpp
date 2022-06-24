#include<iostream>
#include<deque>
using namespace std;
int main(void) {
	int N;
	cin >> N;
	deque<int> d;
	for (int i = 1; i <= N; i++)
		d.push_front(i);
	for (int i = 0; i < N - 1; i++) {
		d.pop_back();
		d.push_front(d.back());
		d.pop_back();
	}
	cout << d.back();
}