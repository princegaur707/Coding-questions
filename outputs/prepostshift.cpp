#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
int array[10] = {3, 0, 8, 1, 12, 8, 9, 2, 13, 10};
int x, y, z;
x = ++array[2];
y = array[2]++;
z = array[x++]; //x will be 10 as it is being increased here also
printf("%d %d %d", x, y, z);  

return 0;
}