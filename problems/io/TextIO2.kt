package io

import com.google.gson.Gson
import java.io.File
import java.io.FileWriter

/*
File design type
word = (type) description
word1 = (type) description
 */

fun main(args: Array<String>) {
    try {
        val inputName = "input.txt"
        val outputName = "Output.json"
        val path = "D:/Android/test/"
        val inputFile = File("$path$inputName")
        val outputFile = File("$path$outputName")
        val gson = Gson()

        //create a list
        val list = ArrayList<Model>()

        for (string in inputFile.bufferedReader(bufferSize = 4096).readLines()) {
            var stringBuilder = StringBuilder()
            for (char in string) {
                if (char == '=') {
                    break
                }
                stringBuilder.append(char)
            }
            val word = stringBuilder.toString().trim()

            //types
            val typesData = string.removePrefix(word).trim()
            stringBuilder = StringBuilder()
            for (char in typesData){
                if (char == ')') {
                    break
                }
                stringBuilder.append(char)
            }
            val type = stringBuilder.toString().removePrefix("= (")

            val des = typesData.removePrefix("= ($type)").trim()

            val model = Model(word,type,des)
            list.add(model)
        }

        //convert list to json string
        val string = gson.toJson(list)
        //crate new file
        outputFile.createNewFile()
        //now write
        val writer = FileWriter(outputFile)
        writer.write(string)
        //close writer
        writer.close()

        println("Done")

    } catch (e: Exception) {
        e.printStackTrace()
    }

    class Model(
            val word:String,
            val type:String,
            val des:String
    )
}

