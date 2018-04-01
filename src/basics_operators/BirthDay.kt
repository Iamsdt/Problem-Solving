package basics_operators

import java.util.*


fun main(args: Array<String>) {

    val sc = Scanner(System.`in`)

    var tCases = sc.nextInt()
    while (tCases > 0) {
        val friends = sc.nextInt()
        val chocolates = sc.nextInt()
        if (chocolates % friends == 0) {
            println("Yes")
        } else {
            println("No")
        }
        tCases--
    }
}