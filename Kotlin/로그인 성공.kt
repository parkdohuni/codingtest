class Solution {
    fun solution(id_pw: Array<String>, db: Array<Array<String>>): String {
        var answer: String = ""
        db.forEach {
            if(id_pw[0] == it[0]) {
                if(id_pw[1] == it[1]){
                    answer = "login"
                    return answer
                } else if(id_pw[1] != it[1]) {
                    answer = "wrong pw"
                    return answer
                }
            } else if(id_pw[0] != it[0]) {
                answer = "fail"
            }
        }
        return answer
    }
}
//다른 사람 풀이
class Solution {
    fun solution(id_pw: Array<String>, db: Array<Array<String>>): String {
        val user = db.find { it[0] == id_pw[0] } ?: return "fail"
        if (user[1] == id_pw[1])
            return "login"
        return "wrong pw"
    }
}