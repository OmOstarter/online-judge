#include <iostream>
using namespace std;
int table[6];
void bottom_up();
void stair_claiming();
int main(){
    stair_claiming();
}
void bottom_up()
{
    table[0] = 1;
    table[1] = 1;
    for(int i = 2; i <= 5; i++)
        table[i] = table[i - 1] + table[i - 2];
}
void stair_claiming()
{
    bottom_up();
    int n;
    while(cin >> n &&(n >=0 && n <= 5))
    {
        cout << "爬到" << n << "階，" << table[n] << "種踏法" << endl;
    }
    
}
/*
http://web.ntnu.edu.tw/~algo/DynamicProgramming.html
bottom-up來求爬梯遞迴
f(n)=
1, n = 1
2, n = 2
f(n-1) + f(n-2), n > 2
*/