#include <iostream>
using namespace std;
int table[10][10];//C(9,9)
int f(int n); 
void Pascal_formula();
int main(){
    Pascal_formula();
}
int f(int n, int m)
{
    if (m == 0 || n == m) 
        return table[n][m] = 1;
    else if(m == 1)
        return table[n][m] = n;
    else if(table[n][m] != 0)
        return table[n][m];
    else
        return table[n][m] = f(n-1,m) + f(n-1,m-1);
}
void Pascal_formula()
{
    for(int index1=0; index1 <= 9; index1++)
        for(int index2 = 0; index2 <= 9; index2++)
            table[index1][index2] = 0;
    int n ,m;
    cout << "input n, m\n";
    cin >> n >> m;
    f(n,m);
    cout << "C[n][m]=" << table[n][m] << endl;
}
