class Solution {
    fun solution(answers: IntArray): IntArray {
        var answer = intArrayOf()
        var save = ArrayList<Int>()
        var first: Array<Int> = arrayOf(1, 2, 3, 4, 5)
        var second: Array<Int> = arrayOf(2, 1, 2, 3, 2, 4, 2, 5)
        var third: Array<Int> = arrayOf(3, 3, 1, 1, 2, 2, 4, 4, 5, 5)
        var firstCount = 0; var secondCount = 0; var thirdCount = 0
        for(i in answers.indices) {
            if(first[i % 5] == answers[i % answers.size]) firstCount++
            if(second[i % 8] == answers[i % answers.size]) secondCount++
            if(third[i % 10] == answers[i % answers.size]) thirdCount++
        }
        var rank = mutableListOf<Int>()
        rank.add(0, firstCount)
        rank.add(1, secondCount)
        rank.add(2, thirdCount)
        rank.sortDescending()
        var count = 0

        if(rank[0] == firstCount) save.add(count++, 1)
        if(rank[0] == secondCount) save.add(count++, 2)
        if(rank[0] == thirdCount) save.add(count++, 3)
        save.sort()
        answer = save.toIntArray()
        return answer
    }
}