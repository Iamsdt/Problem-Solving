package hacker_rank.data_structure.stack

import java.util.*


fun main() {
    val sc = Scanner(System.`in`)
    val n = sc.nextInt()
    var max = Integer.MIN_VALUE
    val stack = Stack<StackNode>()

    for (i in 0 until n) {
        val choice = sc.nextInt()
        if (choice == 1) {
            val value = sc.nextInt()
            max = Math.max(value, max)

            stack.add(StackNode(value, max))
        } else if (choice == 2) {
            if (!stack.isEmpty())
                stack.pop()
            // reset max
            max = if (stack.isEmpty()) Integer.MIN_VALUE
            else stack.peek().max
        } else if (choice == 3) {
            if (!stack.isEmpty()) {
                System.out.println(stack.peek().max)
            }
        }
    }
    sc.close()
}

class StackNode(val int: Int, val max: Int)