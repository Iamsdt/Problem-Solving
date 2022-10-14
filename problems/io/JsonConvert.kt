package io

import com.google.gson.Gson
import com.google.gson.annotations.SerializedName
import java.io.File
import java.io.FileWriter
import java.util.*

/*
Problem is remove a entry from json
json {
        "word":"word1",
        "des":"description",
        "img":""
    }

Expected json
{
    "word":"Word1",
    "des":"description",
}

 */


fun main(args: Array<String>) {
    try {
        val name = "sample.json"
        val output = "data.json"
        val path = "D:/Android/"
        val file = File("$path$name")

        //val bufferReader = BufferedReader(FileReader(file))

        //val text: String = bufferReader.readText()

        val gson = Gson()

        val data = gson.fromJson(file.bufferedReader(bufferSize = 4096),
                Pojo::class.java)

        val list: ArrayList<NEW> = ArrayList()
        for (collection in data.collection) {
            var word = collection.word
            val des = collection.des

            if (word.isEmpty()) continue

            //capital word
            val cap = word[0].toUpperCase()
            word = word.replaceFirst(word[0], cap)

            val newData = NEW(word, des)
            list.add(newData)
        }

        println("Compare size: ${data.collection.size} and ${list.size}")

        println(list[95].word)

        val outputData = Output("favourite",Date().time,list)

        val string = gson.toJson(outputData)

        val outputFile = File("$path$output")
        outputFile.createNewFile()
        val writer = FileWriter(outputFile)
        writer.write(string)
        writer.close()

        println("Done")

        println("Start opening recently closed file")
        val jsonFile = File("$path$output")
        println("File exists: ${jsonFile.exists()}")

        val json = gson.fromJson(jsonFile.bufferedReader(bufferSize = 4096),
                Output::class.java)

        println("Type:${json.type}")
        println("Date:${Date(json.date)}")
        println("List size:${json.list.size}")

    } catch (e: Exception) {
        e.printStackTrace()
    }
}


data class Pojo(
        @SerializedName("volume") val volume: Int,
        @SerializedName("collection") val collection: List<Collection>
)

data class Collection(
        @SerializedName("word") val word: String,
        @SerializedName("des") val des: String,
        @SerializedName("img") val img: String)

class NEW(
        @SerializedName("word") val word: String,
        @SerializedName("des") val des: String

)

class Output(
        @SerializedName("type") val type: String,
        @SerializedName("date")val date: Long,
        @SerializedName("list")val list: List<NEW>)