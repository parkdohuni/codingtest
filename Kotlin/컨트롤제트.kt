class Solution {
    fun solution(s: String): Int {
        var answer: Int = 0
        var num = mutableListOf<Int>()
        var token = s.split(' ')
        for(i in 0 until token.size) {
            if(token[i] == "Z") {
                answer -= token[i - 1].toInt()
            } else {
                answer += token[i].toInt()
            }
        }
        return answer
    }
}