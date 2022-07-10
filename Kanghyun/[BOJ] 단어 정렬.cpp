#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<utility>
using namespace std;
int main() {
	int N;
	cin >> N;
	vector<pair<int, string>> words;
	for (int i = 0; i < N; i++) {
		string word;
		cin >> word;
		words.push_back(pair<int, string>(word.length(), word));
	}
	sort(words.begin(),words.end());
	words.erase(unique(words.begin(), words.end()), words.end());
	for (int i = 0; i < words.size(); i++)
		cout << words[i].second<<"\n";
}