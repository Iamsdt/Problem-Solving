package hacker_rank.data_structure.array


fun main(args: Array<String>) {

    val arr = Array(6) { _ -> Array(6) { 0 } }

    for (i in 0 until 6) {
        val s = readLine() ?: ""
        arr[i] = s.split(" ").map { it.trim().toInt() }.toTypedArray()
    }

    // array with size 16
    //16 block
    val sum = IntArray(16)
    var p = 0

    for (i in 0..3) { //first 3
        //2D array
        for (j in 0..3) {
            //comment first case only
            // 0,0      0,1      0,2
            val f = arr[i][j] + arr[i][j + 1] + arr[i][j + 2]
            //  1,1
            val m = arr[i + 1][j + 1]
            //2,0    2,1     2,2
            val l = arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]

            sum[p] = f + m + l

            p++
        }
    }

    sum.sort()

    //last value of the array
    println(sum[15])
}
