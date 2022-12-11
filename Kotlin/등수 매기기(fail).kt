class Solution {
    fun solution(score: Array<IntArray>): IntArray {
        var answer = mutableListOf<Int>()
        var avgScore = mutableListOf<Int>()
        var sortScore = mutableListOf<Int>()

        score.forEach { avgScore.add(it.sum()) }
        sortScore.addAll(avgScore)
        sortScore.sortDescending()

        avgScore.forEach {
            for (i in sortScore.indices) {
                if (it == sortScore[i]) {
                    answer += i + 1
                    break
                }
            }
        }

        return answer.toIntArray()
    }
}
//class Solution {
//    fun solution(score: Array<IntArray>): IntArray {
//        return score.map(IntArray::average).map { score.map(IntArray::average).sortedDescending().indexOf(it) + 1 }.toIntArray()
//    }
//}
//class Solution {
//    fun solution(score: Array<IntArray>): IntArray {
//        val scoreList = score.map { it.average() }
//        return scoreList.map { curScore ->
//            scoreList.count { it > curScore } + 1
//        }.toIntArray()
//    }
//}
