#include <iostream>
#include <stack>
#include <string>
#include <vector>
#include <sstream>
using namespace std;

int main(void) {
	int N;
	cin >> N;
	stack<int> stk;
	vector<int> v(N, -3);
	cin.ignore();
	
	for (int i = 0; i < N; i++) {
		string tmp;
		getline(cin, tmp);

		if (tmp == "pop")
			if (stk.empty())
				v[i] = -1;
			else
			{
				v[i] = stk.top();
				stk.pop();
			}
		else if (tmp == "size")
			v[i] = stk.size();
		else if (tmp == "empty")
			if (stk.empty())
				v[i] = 1;
			else
				v[i] = 0;
		else if (tmp == "top")
			if (stk.empty())
				v[i] = -1;
			else
				v[i] = stk.top();
		else
		{
			string str = tmp, k;
			stringstream ss(str);
			vector<string> strv;
			while (ss >> k)
				strv.push_back(k);
			stk.push(stoi(strv[1]));
		}
	}

	for (int i = 0; i < N; i++) 
		if(v[i] != -3)
			cout << v[i] << "\n";
	
}