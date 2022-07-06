#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int Rank(int n) {
    int rank = 6;
    if (n == 6)
        rank = 1;
    else if (n == 5)
        rank = 2;
    else if (n == 4)
        rank = 3;
    else if (n == 3)
        rank = 4;
    else if (n == 2)
        rank = 5;
    return rank;
}

vector<int> solution(vector<int> lottos, vector<int> win_nums) {
    vector<int> answer;
    int same_numbers = 0;
    int unidentified = 0;

    for (int i = 0; i < 6; i++)
        if (*find(win_nums.begin(), win_nums.end(), lottos[i]) == lottos[i])
            same_numbers += 1;

    for (int i = 0; i < 6; i++)
        if (lottos[i] == 0)
            unidentified++;
    int max = same_numbers + unidentified;
    
    answer.push_back(Rank(max));
    answer.push_back(Rank(same_numbers));

    return answer;
}