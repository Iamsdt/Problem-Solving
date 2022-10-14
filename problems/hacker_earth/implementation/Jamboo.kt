package hacker_earth.implementation

fun main(args: Array<String>) {
    val s = readLine()
    val b = StringBuilder()
    var l = s!!.length - 1
    while (l >= 0){
        b.append(s[l])
        l--
    }
    println(b)
}