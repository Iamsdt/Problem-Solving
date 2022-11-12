package hacker_earth.basic_input_output

fun main(args: Array<String>) {

    val times = readLine()?.toInt() ?: 0

    for (i in 0 until times){
        val input = readLine() ?: "abc bca"

        val list = input.split(" ")

        val s1 = list[0]
        val s2 = list[1]

        val s = StringBuilder()

        for(j in s1){
            if (s2.contains(j)) {
                s.append(j)
            }
        }

        if (s1 == s.toString()){
            println("YES")
        } else{
            println("NO")
        }
    }

}