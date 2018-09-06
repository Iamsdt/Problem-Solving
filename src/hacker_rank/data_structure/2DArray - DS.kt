package hacker_rank.data_structure

import java.util.*

fun hourglassSum(arr: Array<Array<Int>>): Int {


    return 0
}

fun main(args: Array<String>) {
    val scan = Scanner(System.`in`)

    val arr = Array(6) { _ -> Array(6) { 0 } }

    for (i in 0 until 6) {
        arr[i] = scan.nextLine().split(" ").map { it.trim().toInt() }.toTypedArray()
    }

    val result = hourglassSum(arr)

    println(result)
}