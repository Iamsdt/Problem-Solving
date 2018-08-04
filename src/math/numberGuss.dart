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