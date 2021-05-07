function solution(s) {
    let answer = 0;
    let count = 0;
    s = s.split('');
    while(count < s.length) {
        let stack = [];
        let right = true;
        for (let i=0; i<s.length; i++) {
            if (s[i] === '(' || s[i] === '{' || s[i] === '[') stack.push(s[i]);
            else {
                const close = stack.pop();
                if ((s[i] === ')' && close !== '(') || (s[i] === '}' && close !== '{') || (s[i] === ']' && close !== '[') || close === undefined) {
                    right = false;
                    break;
                }
            }
        }
        if (right && stack.length === 0) answer += 1;
        const shift = s.shift();
        s.push(shift);
        count += 1;
    }

    return answer;
}

console.log(solution("[](){}"));