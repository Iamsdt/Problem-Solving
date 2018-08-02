package extra

import com.google.gson.Gson
import com.google.gson.annotations.SerializedName
import java.io.File
import java.io.FileWriter

/*
Problem is remove a entry from json
json {
"word":"word1",
"des":"description",
"img"
}

Expected json
{
"word":"Word1",
"des":"description",
}

 */


fun main(args: Array<String>) {
    try {
        val name = "Sample.json"
        val output = "Output.json"
        val path = "D:/Android/"
        val file = File("$path$name")

        //val bufferReader = BufferedReader(FileReader(file))

        //val text: String = bufferReader.readText()

        val gson = Gson()

        val data = gson.fromJson(file.bufferedReader(bufferSize = 4096), Pojo::class.java)

        val list: ArrayList<NEW> = ArrayList()
        for (collection in data.collection) {
            var word = collection.word
            val des = collection.des

            //capital word
            val cap = word[0].toUpperCase()
            word = word.replaceFirst(word[0],cap)

            val newData = NEW(word, des)
            list.add(newData)
        }

        println("Compare size: ${data.collection.size} and ${list.size}")

        println(list[95].word)

        val string = gson.toJson(list)

        val outputFile = File("$path$output")
        outputFile.createNewFile()
        val writer = FileWriter(outputFile)
        writer.write(string)
        writer.close()

        println("done from thread")


        println("Done")

    } catch (e: Exception) {
        e.printStackTrace()
    }
}


data class Pojo(
        @SerializedName("volume") val volume: Int,
        @SerializedName("collection") val collection: List<Collection>
)

data class Collection(
        @SerializedName("img") val img: String,
        @SerializedName("des") val des: String,
        @SerializedName("word") val word: String
)

class NEW(
        val word: String,
        val des: String
)