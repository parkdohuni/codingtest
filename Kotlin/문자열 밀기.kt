class Solution {
    fun solution(A: String, B: String): Int {
        var answer: Int = 1
        var save = mutableListOf<String>()
        var tempA: String = A
        var change: String
        if(A.equals(B)) {
            return 0
        }
        for(i in 0 until A.length) {
            save.add(0, tempA[A.length - 1].toString())
            for(j in 1 until A.length) {
                save.add(j, tempA[j - 1].toString())
            }
            change = save.joinToString("", "", "")
            if(B.equals(change)){
                return answer
            } else {
                tempA = save.joinToString("", "", "")
                save.clear()
                answer++
            }
        }
        return -1
    }
}
//다른 사람 풀이
class Solution {
    fun solution(A: String, B: String): Int = (B + B).indexOf(A)
    //hel lohel lo
    //012 34567 89
    //lohel
}