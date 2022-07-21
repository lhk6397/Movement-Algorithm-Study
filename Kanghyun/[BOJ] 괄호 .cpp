#include <iostream>
#include <stack>
#include <vector>
#include <string>
using namespace std;
int main(void) {
	int T;
	cin >> T;

	string brakets;
	vector<string> ans;

	for (int i = 0; i < T; i++) {
		stack<char> stk;
		cin >> brakets;
		bool success = true;
		for (int j = 0; j < brakets.length(); j++) {
			if (brakets[j] == '(')
				stk.push(brakets[j]);
			else
				if (!stk.empty() && stk.top() == '(')
					stk.pop();
				else {
					success = false;
					break;
				}
					

		}
		if (stk.empty() && success)
			ans.push_back("YES");
		else
			ans.push_back("NO");
	}

	for (int i = 0; i < T; i++) 
		cout << ans[i]<< "\n";
	
}