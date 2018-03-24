package basic_input_output

    fun main(args: Array<String>) {

        val s = readLine() ?: ""

        if (check(s)) {
            println("YES")
        } else {
            println("NO")
        }

    }

    fun check(s: String): Boolean {
        var i1 = 0
        var i2 = s.length - 1

        while (i2 > i1) {
            if (s[i1] != s[i2]) {
                return false
            }
            ++i1
            --i2
        }
        return true
    }
}