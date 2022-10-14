package hacker_rank.month

fun main(args: Array<String>) {

    var n = readLine()?.trim()?.toInt() ?: 0

    var count = 0

    var max = 0

    while (n > 0) {
        val rem = n % 2
        if (rem == 1)
            count++
        else
            count = 0

        max = if (count >= max) count else max;

        n /= 2
    }

    println(max)

}