package hacker_rank

import java.util.*

fun main(args: Array<String>) {
    val scan = Scanner(System.`in`)

    val meal_cost = scan.nextLine().trim().toDouble()

    val tip_percent = scan.nextLine().trim().toInt()

    val tax_percent = scan.nextLine().trim().toInt()

    solve(meal_cost, tip_percent, tax_percent)
}

fun solve(meal_cost: Double, tip_percent: Int, tax_percent: Int): Unit {

    val a = meal_cost * tip_percent / 100
    val b = meal_cost * tax_percent / 100

    val ans = meal_cost + a + b
    val pay = Math.round(ans).toInt()

    println("The total meal cost is $pay dollars.")
}