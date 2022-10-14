package hacker_rank.month

fun main(args: Array<String>) {
    val i = 4
    val d = 4.0
    val s = "HackerRank "

    val int = readLine()?.toInt() ?: 0
    val double = readLine()?.toDouble() ?: 0.0
    val string = readLine() ?: ""

    var r= d+double

    r = Math.round(r * 10.0) / 10.0

    println(i + int)
    println(r)
    println(s + string)
}