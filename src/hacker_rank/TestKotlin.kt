package hacker_rank

fun main(args: Array<String>) {

    val n = readLine()?.trim()?.toInt() ?: 0

    when {
        n % 2 != 0 -> println("Weird")
        n in 2..5 -> println("Not Weird")
        n in 6..20 -> println("Weird")
        n > 20 -> println("Not Weird")
    }

    main(emptyArray())

}
