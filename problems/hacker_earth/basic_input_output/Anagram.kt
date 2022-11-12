package hacker_earth.basic_input_output

import java.util.*

fun main(args: Array<String>) {

    val t = readLine()!!.toInt()
    var unique = 0

    val input = Scanner(System.`in`)

    for (i in 0 until t) {
        val word1 = input.nextLine()
        val word2 = readLine()

        for (m in word1!!.asIterable()) {
            for (n in word2!!.asIterable()) {
                if (m == n) {
                    unique++
                }
            }
        }

        println(word1.length + word2!!.length - 2 * unique)
    }
}