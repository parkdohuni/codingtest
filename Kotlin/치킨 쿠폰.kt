class Solution {
    fun solution(chicken: Int): Int {
        var answer: Int = 0
        var coupon: Int = 0
        var chickenNum: Int = chicken
        while (chickenNum / 10 != 0) {
            coupon += chickenNum % 10
            chickenNum /= 10
            answer += chickenNum
            chickenNum += coupon
            coupon = 0
        }
        return answer
    }
}