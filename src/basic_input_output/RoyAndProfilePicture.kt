package basic_input_output

import java.util.*

@Throws(Exception::class)
fun main(args: Array<String>) {

    val input = Scanner(System.`in`)

    val length = input.nextInt()

    val noPhotos = input.nextInt()

    var height: Int
    var width: Int

    for (i in 0 until noPhotos) {

        width = input.nextInt()
        height = input.nextInt()

        if (width == height && width > length && height > length)
            println("ACCEPTED")
        else if (width < length || height < length)
            println("UPLOAD ANOTHER")
        else if (width == length && height == length)
            println("ACCEPTED")
        else if (width >= length && height >= length)
            println("CROP IT")
    }
}

/**
 * Roy wants to change his profile picture on Facebook. Now Facebook has some restriction over the dimension of picture that we can upload.
Minimum dimension of the picture can be L x L, where L is the length of the side of square.

Now Roy has N photos of various dimensions.
Dimension of a photo is denoted as W x H
where W - width of the photo and H - Height of the photo

When any photo is uploaded following events may occur:

[1] If any of the width or height is less than L, user is prompted to upload another one. Print "UPLOAD ANOTHER" in this case.
[2] If width and height, both are large enough and
(a) if the photo is already square then it is accepted. Print "ACCEPTED" in this case.
(b) else user is prompted to crop it. Print "CROP IT" in this case.

(quotes are only for clarification)

Given L, N, W and H as input, print appropriate text as output.

Input:
First line contains L.
Second line contains N, number of photos.
Following N lines each contains two space separated integers W and H.

Output:
Print appropriate text for each photo in a new line.

Constraints:
1 <= L,W,H <= 10000
1 <= N <= 1000

SAMPLE INPUT
180
3
640 480
120 300
180 180
SAMPLE OUTPUT
CROP IT
UPLOAD ANOTHER
ACCEPTED
 */
