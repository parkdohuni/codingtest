class Solution {
    fun solution(numbers: IntArray): IntArray {
        var answer: IntArray = intArrayOf()
        var sum = mutableListOf<Int>()
        for(i in numbers.indices) {
            for(j in numbers.indices) {
                if(i == j) continue
                else {
                    sum.add(i, numbers[i] + numbers[j])
                }
            }
        }
        sum.toString()
        sum = sum.distinct() as MutableList<Int>
        sum.sort()
        answer = sum.toIntArray()
        return answer
    }
}