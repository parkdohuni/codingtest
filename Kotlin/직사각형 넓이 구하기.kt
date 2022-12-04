class Solution {
    fun solution(dots: Array<IntArray>): Int {
        var answer: Int = 0
        var horiBig = dots[0][0]
        var horiSmall = dots[0][0]
        var vertiBig = dots[0][1]
        var vertiSmall = dots[0][1]
        dots.forEach {
            if(it[0] > horiBig) {
                horiBig = it[0]
            } else if (it[0] <= horiSmall) {
                horiSmall = it[0]
            }
            if(it[1] > vertiBig) {
                vertiBig = it[1]
            } else if (it[1] <= vertiSmall) {
                vertiSmall = it[1]
            }
        }
        val hori = horiBig - horiSmall
        val verti = vertiBig - vertiSmall
        return hori * verti
    }
}
//다른 사람 풀이
class Solution {
    fun solution(dots: Array<IntArray>): Int {
        val coordX = dots.map { it[0] }.toSortedSet()
        val coordY = dots.map { it[1] }.toSortedSet()

        return (coordX.last() - coordX.first()) * (coordY.last() - coordY.first())
    }
}