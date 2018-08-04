package math

fun main(args: Array<String>) {

    val times = readLine()?.toInt() ?: 0

    for (i in 0 until times){
        var sum = 0
        val number = readLine()?.toInt() ?: 0
        for (num in 1 until number){
            if (number % num == 0){
                sum += num
            }
        }
        println(sum)
    }


}