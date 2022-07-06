#include<iostream>
#include<algorithm>
using namespace std;
int main() {
	int w[10];
	int k[10];
	int wsum = 0, ksum = 0;
	for (int i = 0; i < 10; i++)
		cin >> w[i];
	sort(w, w + 10);
	for (int i = 0; i < 10; i++)
		cin >> k[i];
	sort(k, k + 10);
	for (int i = 0; i < 3; i++) {
		wsum += w[9 - i];
		ksum += k[9 - i];
	}
	cout << wsum << " " << ksum;
}