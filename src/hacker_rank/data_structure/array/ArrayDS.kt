package hacker_rank.data_structure.array

import java.util.*

fun reverseArray(a: Array<Int>): Array<Int> {
    val array = Array(a.size){0}

    for ((p, i) in (a.size - 1 downTo 0).withIndex()){
        array[p] = a[i]
    }
    return array
}

fun main(args: Array<String>) {
    val scan = Scanner(System.`in`)

    val arrCount = scan.nextLine().trim().toInt()

    val arr = scan.nextLine().split(" ")
            .map { it.trim().toInt() }.toTypedArray()

    val res = reverseArray(arr)

    println(res.joinToString(" "))
}