#include <iostream>
#include <string>
using namespace std;

int big(int i, int j);
int main() {
	int N;
	cin >> N;
	int v1 = 0 , v2 = 0, v3 = 0, v4 = 0, v5 = 0, v6 = 0, v7 = 0, v8 = 0, v0 = 0;
	string room = to_string(N);
	for (int i = 0; i < room.size(); i++)
		if (room[i] == '1')
			v1++;
		else if (room[i] == '2')
			v2++;
		else if (room[i] == '3')
			v3++;
		else if (room[i] == '4')
			v4++;
		else if (room[i] == '5')
			v5++;
		else if (room[i] == '7')
			v7++;
		else if (room[i] == '8')
			v8++;
		else if (room[i] == '0')
			v0++;
		else
			v6++;
	v6 = v6 / 2 + v6 % 2;
	int max = v1;
	max = big(max, v2);
	max = big(max, v3);
	max = big(max, v4);
	max = big(max, v5);
	max = big(max, v6);
	max = big(max, v7);
	max = big(max, v8);
	max = big(max, v0);
	cout << max;
}

int big(int i, int j) {
	int b;
	if (i >= j)
		b = i;
	else
		b = j;
	return b;
}