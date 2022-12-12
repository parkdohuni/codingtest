class Solution {
    fun solution(N: Int, stages: IntArray): IntArray {
        var answer = intArrayOf()
        var size = stages.size
        var result = mutableListOf<Double>()
        var save = mutableListOf<Double>()
        var answers = mutableListOf<Int>()
        var num = 1
        var count = 0
        stages.sort()
        for(index in 0 until N) {
            for(i in stages) {
                if(i == num) {
                    count++
                }
            }
            if(size == 0) {
                result.add(index, 0.0)
            } else {
                result.add(index, (count.toDouble() / size.toDouble()))
                size -= count
                num++
                count = 0
            }
        }
        save.addAll(result)
        result.sortDescending()
        var index = 0
        for(i in 0 until N) {
            for(j in 0 until N) {
                if (result[i] == save[j]) {
                    answers.add(index, j + 1)
                    index++
                    save[j] = -1.0
                    break
                }
            }
        }
        answer = answers.toIntArray()
        return answer
    }
}
//[3,4,2,1,5]