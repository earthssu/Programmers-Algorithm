function solution(n) {
    let answer = 0;
    let first = 1;
    let second = 2;
    if (n < 3) return n;

    for (let i=3; i<=n; i++) {
        answer = (first + second) % 1234567;
        first = second;
        second = answer;
    }
    return answer;
}