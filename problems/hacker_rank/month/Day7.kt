package hacker_rank.month

import java.util.*

fun main(args: Array<String>) {
    val scan = Scanner(System.`in`)

    val n = scan.nextLine().trim().toInt()

    val arr = scan.nextLine().split(" ")
            .map { it.trim().toInt() }.toTypedArray()

    //simply
    //arr.reverse()

    for (i in n - 1 downTo 0) {
        print("${arr[i]} ")
    }
}