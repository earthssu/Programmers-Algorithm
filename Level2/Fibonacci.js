function solution(n) {
    let answer = 0;
    let fir = 0;
    let sec = 1;
    for (let i = 2; i <= n; i++) {
        if (i < 2) answer = i;
        else {
            answer = (fir + sec) % 1234567;
            fir = sec;
            sec = answer;
        }
    }
    return answer % 1234567;
}