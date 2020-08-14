package hacker_earth.math

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

fun main(args: Array<String>) {

    val times = readLine()?.toInt() ?: 0

    for (i in 0 until times){
        var sum = 0
        val number = readLine()?.toInt() ?: 0
        for (num in 1 until number){
            if (number % num == 0){
                sum += num
            }
        }
        println(sum)
    }


}