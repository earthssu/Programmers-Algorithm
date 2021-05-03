function solution(n) {
    let answer = 1;
    let start = 1;
    while (start < n) {
        let sum = 0;
        let plus = start;
        while (sum < n) {
            sum += plus;
            plus += 1;
        }
        if (sum === n) answer += 1;
        start += 1;
    }
    return answer;
}