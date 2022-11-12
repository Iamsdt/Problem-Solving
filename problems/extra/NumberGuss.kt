package extra

//problem is
/*
x, y z, is integer value

    x y z
    x y z
    x y z
   -------
   +z z z

    1)Find the value of x, y, z
    2) where z != 0
    3) where x != 0

 */

fun main(args: Array<String>) {

    loop@for (x in 1 until 100){
        for (y in 0 until 100){
            for (z in 0 until 100){
                val a:Int = "$x$y$z".toInt()
                val ans:Int = "$z$z$z".toInt()
                val calculate = a * 3
                if (calculate == ans){
                    println("X: $x, Y: $y, Z: $z")
                    break@loop
                }
            }
        }
    }

}

/*
    Answer
    1) x = 0, y = 0, z = 0;
    2) x = 0, y = 18, z = 5;
    3) x = 1, y = 8, z = 5;

 */