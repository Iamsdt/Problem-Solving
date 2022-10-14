package hacker_rank.month


fun main(args: Array<String>) {

    val num = readLine()?.trim()?.toInt() ?:0

    for (i in 0 until num){
        val string = readLine() ?: ""

        val even = StringBuilder()
        val odd = StringBuilder()

        for (j in 0 until string.length){

            if ((j % 2) == 0){
                odd.append(string[j])
            } else{
                even.append(string[j])
            }
        }

        println("$odd $even")


    }

}
