function solution(s) {
    const answer = [0, 0];

    while (s !== '1') {
        answer[0] += 1;
        const len = s.length;
        s = s.replace(/0/g, '');
        answer[1] += len - s.length;
        s = s.length.toString(2);
    }

    return answer;
}