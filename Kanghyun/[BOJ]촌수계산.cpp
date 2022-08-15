#include<iostream>
#include<queue>
using namespace std;
bool adj[101][101] = { 0, };
int visited[101] = { 0, };
queue<int> q;
int main() {
	int n, m, one, another;
	cin >> n;
	cin >> one >> another;
	cin >> m;
	for (int i = 0; i < m; i++) {
		int x, y;
		cin >> x >> y;
		adj[x][y] = true; adj[y][x] = true;
	}
	q.push(one);
	visited[one] = 0;
	while (!q.empty() && visited[another] == 0) {
		for (int i = 1; i <= n; i++)
			if (adj[q.front()][i] == true && visited[i] < 1)
			{
				q.push(i);
				visited[i] = visited[q.front()] + 1;
			}
		q.pop();
	}
	if (visited[another] == 0)
		cout << -1;
	else
		cout << visited[another];
}