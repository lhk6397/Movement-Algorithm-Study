#include<iostream>
#include<queue>
using namespace std;
int N, M, V;
bool visited[1000] = { 0, };
bool adj[1000][1000] = { 0, };
void dfs(int d);
void bfs(int b);

int main() {
	cin >> N >> M >> V;

	for (int i = 0; i < M; i++) {
		int a, b;
		cin >> a >> b;
		adj[a - 1][b - 1] = true;
		adj[b - 1][a - 1] = true;
	}
	visited[V - 1] = true;
	dfs(V - 1);
	cout << "\n";
	for (int i = 0; i < 1000; i++) {
		visited[i] = 0;
	}
	bfs(V - 1);
}

void dfs(int d) {
	cout << d + 1 << " ";

	for (int next = 0; next < N; next++) {
		if (adj[d][next] && !visited[next])
		{
			visited[next] = true;
			dfs(next);
		}
	}
}

void bfs(int b) {
	
	queue<int> q;
	visited[b] = true;
	q.push(b);

	while (!q.empty()) {
		int now = q.front();
		cout << q.front() + 1 << " ";
		q.pop();
		for (int i = 0; i < N; i++) {
			int next = i;
			if (adj[now][next] && !visited[next]) {
				visited[next] = true;
				q.push(next);
			}
		}
	}
}