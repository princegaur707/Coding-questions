#include<iostream>
#include<stdio.h>
using namespace std;
int main(){
      int a=2;
      switch(a)
      {
      case 1: printf("A");
      case 2: printf("B");
      case 3: printf("C");//till now break have not came so we can print this 
      break;
      case 4: printf("D");
      default: printf("E");
      break;
      }
}