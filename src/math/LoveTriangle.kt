package math

fun main(args: Array<String>) {

    var input = readLine()?.toInt() ?: 0
    while (input != 0){
        println(find(input))
        input = readLine()?.toInt() ?: 0
    }
}

fun find(input: Int): Int {
    return if (input < 9) input
    else
        input % 9 + 10 * find(input / 9)
}