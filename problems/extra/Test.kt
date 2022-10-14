package extra

import java.math.RoundingMode

fun main(args: Array<String>) {

    val list:ArrayList<Pro> = ArrayList()

    list.add(Pro(1,70.0,70.0))
    list.add(Pro(2,70.0,70.0))
    list.add(Pro(3,70.0,60.0))
    list.add(Pro(4,70.0,70.0))
    list.add(Pro(5,70.0,50.0))
    list.add(Pro(6,70.0,70.0))
    list.add(Pro(7,70.0,40.0))
    list.add(Pro(8,70.0,70.0))
    list.add(Pro(9,70.0,60.0))
    list.add(Pro(10,70.0,70.0))

    val data: Array<DataPoint> = Array(list.size+1) { DataPoint(0.0,0.0) }
    data[0] = DataPoint(0.0,0.0)
    var index = 1

    list.forEach {
        val week = it.week
        val budget = it.budget
        val complete= it.complete

        val div = complete/budget

        var plot = (div * week) / 10 //divided with 10 to keep minimum

        plot = plot.toBigDecimal()
                .setScale(2, RoundingMode.UP)
                .toDouble()

        data[index] = DataPoint(plot,plot)
        index +=1
    }

    data.forEach { println(it.x) }

}

class DataPoint(val x:Double,val y:Double)

class Pro(val week:Int,val budget:Double, val complete:Double)