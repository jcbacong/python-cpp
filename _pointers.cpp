#include <iostream>
#include <stdlib.h>
#include "_pointers.h"
using namespace std;

void hello_world(){
	cout << "Hello world!" <<endl;
	}

Point* frames(float *a, float *b, int count){
	Point* P;
	P = (Point*)malloc(sizeof(Point)*count);
	for(int i=0; i<count; i++){
		P[i].m = a[i];
		P[i].t = b[i];
	}
	return P;
}

int main(){

}