package basic_input_output

fun main(args: Array<String>) {

    while (true){
        val input = readLine()?.toInt() ?: 0
        if (input == 42){
            break
        }else{
            println(input)
        }
    }

    //link
    //https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/life-the-universe-and-everything/

}