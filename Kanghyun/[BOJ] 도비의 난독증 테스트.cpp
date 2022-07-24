#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;
int main() {
	int n;
	vector<string> print;
	while (1) {
		vector<pair<string,int>> dic;
		vector<string> sv;
		cin >> n;
		if (n == 0)
			break;
		int m = n;
		while (m != 0) {
			string word;
			cin >> word;                   //단어 입력
			sv.push_back(word);
			int k = word.length();
			for (int i = 0; i < k; i++) 
				if (word[i] <= 90)
					word[i] += 32;
			pair<string,int> www;
			www.first = word;
			www.second = n - m;
			dic.push_back(www);
			m--;
		}
		sort(dic.begin(), dic.end());
		int index = dic[0].second;
		print.push_back(sv[index]);
	}
	int leng = print.size();
	for (int i = 0; i < leng; i++)
		cout << print[i] <<"\n";
}