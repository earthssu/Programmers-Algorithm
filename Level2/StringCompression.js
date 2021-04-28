function solution(s) {
    const len = s.length;
    let answer = len;
    let str = String(s);
    for (let i=1; i<=Math.floor(len/2); i++) {
        let strArr = [];
        let count = 0;
        while (count < len) {
            strArr.push(str.substr(count, i));
            count += i;
        }
        let match = strArr[0];
        let num = 1;
        let result = '';
        strArr.slice(1).forEach((a) => {
            if (match === a) {
                num += 1;
            }
            else {
                num = num > 1 ? String(num) : '';
                result += num + match;
                match = a;
                num = 1;
            }
        })
        num = num > 1 ? String(num) : '';
        result += num + match;
        answer = Math.min(answer, result.length);
    }
    return answer;
}