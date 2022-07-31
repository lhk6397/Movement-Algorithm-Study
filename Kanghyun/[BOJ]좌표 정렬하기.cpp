#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
int main() {
	int N;
	vector<pair<int, int>> points;
	cin >> N;
	for (int i = 0; i < N; i++) {
		pair<int, int> point;
		int x, y;
		cin >> x >> y;
		point.first = x; point.second = y;
		points.push_back(point);
	}
	sort(points.begin(), points.end());
	for (int i = 0; i < N; i++) 
		cout << points[i].first << " " << points[i].second << "\n";
}