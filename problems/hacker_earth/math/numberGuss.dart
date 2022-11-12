import 'dart:io';

void main(){

	int times = int.parse(stdin.readLineSync());

	for (var i = 0; i < times; i++) {
		var sum = 0;
		int number = int.parse(stdin.readLineSync());

		int j = 1;
		while(number > j){
			if (number % j == 0){
				sum += j;
			}

			j++;
		}

		print(sum);
	}

}

/*
Find the logic from the given sample input/output.

And answer Q queries.

Constraints :

1 <= Value <= 100000
1<=nunber of query<=10000

SAMPLE INPUT   SAMPLE OUTPUT
8
10  8
30  42
45  33
9   4
69  27
77  19
127 1
150 222
 */