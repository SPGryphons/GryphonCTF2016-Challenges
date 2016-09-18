// ConsoleApplication3.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>
using namespace std;

//Prevent xxd the flag straight away
void decode(string& c, int a[]) {
	for (int i = 0, j = 0; c[j]; j++, i = (i + 1) % 7) {
		c[j] -= a[i];
		if (c[j] < 32) c[j] += 90;
	}
}

int main()
{
	string inputpass;
	string fakeflag = "GCTF{Not_So_Easy}";
	string flag= "f:t6v\"b5>e74b85vvni6";
	cout << "QR demands a secret password" << endl;
	cin >> inputpass;
	if (inputpass == "SwegLord_1996") {
		cout << "Congratz M8 here's your flag " << endl;
		int a[] = { 4, 9, 6, 2, 4, 3, 3 }; //Array to decrypt
		decode(flag,a);
		cout << flag <<endl;
		cout << "Please encapsulate the flag with GCTF{}" << endl;
	}
	else {
		cout << "oops,try harder? you can do it? believe in yourself? just do it? oops? oops? oops?" << endl;
	}
	system("pause");
	return 0;
}


