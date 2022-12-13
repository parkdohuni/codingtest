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
//다른 사람 풀이
//class Solution {
//    fun solution(N: Int, stages: IntArray): IntArray {
//        var answer = IntArray(N)
//
//        val indexMap: MutableMap<Int, Int> = mutableMapOf()
//        val failureMap: MutableMap<Int, Double> = mutableMapOf()
//        stages.forEach {
//            when (indexMap.containsKey(it)) {
//                true -> indexMap[it] = indexMap.getValue(it) + 1
//                false -> indexMap[it] = 1
//            }
//        }
//        var totalSize = stages.size
//
//        for (i in 1..N) {
//            when (indexMap.containsKey(i)) {
//                true -> {
//                    failureMap[i] = (indexMap.getValue(i) / totalSize.toDouble())
//                    totalSize -= indexMap.getValue(i)
//                }
//                false -> failureMap[i] = 0.0
//            }
//        }
//        val list = failureMap.toList().sortedByDescending { (index, value) -> value }
//
//        for (i in 0 until N) {
//            answer[i] = list[i].first
//        }
//
//        return answer
//    }
//}