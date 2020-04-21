#include<iostream>
#include<stdio.h>
using namespace std;
int main(){
      int a;
      a=1;
      while(a<=10){
            printf("%d",a);
            if(a>3 && a<8)
            continue;
            a++;
      }
      printf("%d",a+10);
}