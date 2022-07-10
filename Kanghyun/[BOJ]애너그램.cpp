#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;
int main() {
	int t;
	cin >> t;
	vector<string> print;
	for (int i = 0; i < t; i++) {
		string first, second;
		cin >> first >> second;
		print.push_back(first);
		print.push_back(second);
		int a = first.length();
		int b = second.length();
		if (a != b)
			print.push_back(" are NOT");
		else{
			vector<char> f;
			vector<char> s;
			while (a != 0) {
				f.push_back(first[a - 1]);
				s.push_back(second[a - 1]);
				a--;
			}
			sort(f.begin(), f.end());
			sort(s.begin(), s.end());
			int j = 0;
			bool k = false;
			while (f[j] == s[j]) {
				j++;
				if (j == b - 1) {
					k = true;
					break;
				}
			}
			if(k == true)
				print.push_back(" are");
			else
				print.push_back(" are NOT");
		}
	}
	for (int i = 0; i < t; i++)
		cout << print[3 * i] <<" & "<< print[3 * i + 1] << print[3 * i + 2] << " anagrams.\n";
}