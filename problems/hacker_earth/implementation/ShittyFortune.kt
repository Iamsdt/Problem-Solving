package hacker_earth.implementation

fun main(args: Array<String>) {

    val time = readLine()?.toInt() ?: 0
    val output = StringBuilder()

    for (t in 0 until time){

        val string = readLine() ?: ""

        var len = string.length - 1

        while (len >= 0){
            output.append(string[len])
            len--
        }

        if (string == output.toString()){
            println("YES")
        } else{
            println("NO")
        }

    }


}