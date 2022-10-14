package hacker_earth.implementation

fun main(args: Array<String>) {
    val i = readLine()!!.toInt()
    var s = 0
    for (p in 0 until i) {

        val j = readLine()!!.toInt()

        if (j >= 0) {
            s += j
        }
    }
    println(s)
}