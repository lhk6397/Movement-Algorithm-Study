#include <string>
#include <vector>
#include <iostream>

using namespace std;

string solution(vector<int> numbers, string hand) {
    string answer = "";

    int keypad[4][12] = {
        {3, 1, 0, 1, 2, 1, 2, 3, 2, 3, 4, 4},
        {2, 2, 1, 2, 1, 0, 1, 2, 1, 2, 3, 3},
        {1, 3, 2, 3, 2, 1, 2, 1, 0, 1, 2, 2},
        {0, 4, 3, 4, 3, 2, 3, 2, 1, 2, 1, 1}
    };
    int Lnum = 10, Rnum = 11;
    int press_length = numbers.size();

    for (int i = 0; i < press_length; i++) {
        if (numbers[i] == 1 || numbers[i] == 4 || numbers[i] == 7)
        {
            answer += "L";
            Lnum = numbers[i];
        }
        else if (numbers[i] == 3 || numbers[i] == 6 || numbers[i] == 9)
        {
            answer += "R";
            Rnum = numbers[i];
        }
        else
        {
            if(numbers[i] == 0)
                if (keypad[3][Lnum] < keypad[3][Rnum]){
                    answer += "L";
                    Lnum = numbers[i];
                }
                else if (keypad[3][Lnum] > keypad[3][Rnum]) {
                    answer += "R";
                    Rnum = numbers[i];
                }
                else
                    if (hand == "left") {
                        answer += "L";
                        Lnum = numbers[i];
                    }
                    else {
                        answer += "R";
                        Rnum = numbers[i];
                    }
            else {
                int index = (numbers[i] - 2) / 3;
                if (keypad[index][Lnum] < keypad[index][Rnum]) {
                    answer += "L";
                    Lnum = numbers[i];
                }
                else if (keypad[index][Lnum] > keypad[index][Rnum]) {
                    answer += "R";
                    Rnum = numbers[i];
                }
                else
                    if (hand == "left") {
                        answer += "L";
                        Lnum = numbers[i];
                    }
                    else {
                        answer += "R";
                        Rnum = numbers[i];
                    }
            }
        }
    }
    
    return answer;
}

int main(void) {
    vector <int> numbers = { 1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5 };
    string hand = "right";
    cout << solution(numbers, hand);
}