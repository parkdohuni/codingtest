class Solution {
    fun gcd(a: Int, b:Int): Int = if(b != 0) gcd(b, a % b) else a
    fun div(denominator: Int): Int {
        var quotient: Int = denominator
        while (quotient % 2 == 0) {
            quotient = quotient / 2
        }
        while (quotient % 5 == 0) {
            quotient = quotient / 5
        }
        return quotient
    }
    fun solution(a: Int, b: Int): Int {
        var answer: Int = 2
        if(a / b == 1) return 1
        var gcd = gcd(a, b)
        var denominator: Int = 0
        if(gcd != 1) {
            denominator = (b / gcd).toInt()
        } else {
            denominator = b
        }
        if(div(denominator) == 1) answer = 1
        return answer
    }
}