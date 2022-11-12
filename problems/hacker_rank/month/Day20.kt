package hacker_rank.month

import java.util.Collections.swap

fun main(args: Array<String>) {


    val n = readLine()?.toInt() ?: 0

    val a = IntArray(n)

    val ln = readLine() ?: ""

    val list = ln.split(" ")

    for (i in 0 until list.size) {
        a[i] = list[i].toInt()
    }

    var totalSwaps = 0
    for (i in n - 1 downTo 1) {
        var numberOfSwaps = 0
        for (j in 0 until i) {
            if (a[j] > a[j + 1]) {
                val temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp
                numberOfSwaps++
                totalSwaps++
            }
        }
        if (numberOfSwaps == 0) {
            break
        }
    }
    println("Array is sorted in $totalSwaps swaps.")
    System.out.println("First Element: " + a[0])
    System.out.println("Last Element: " + a[n - 1])
}