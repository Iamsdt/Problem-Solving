package hacker_rank.month


fun main(args: Array<String>) {

    val time = readLine()?.trim()?.toInt() ?: 0

    val map:HashMap<String,Int> = hashMapOf()

    for (n in 0 until time) {
        val add = readLine() ?: ""
        val li = add.split(" ")
        map.put(li[0],li[1].toInt())
    }

    for (n in 0 until time) {
        val key = readLine() ?: ""
        if (map.containsKey(key)){
            println(map[key])
        } else{
            println("Not found")
        }
    }

}
