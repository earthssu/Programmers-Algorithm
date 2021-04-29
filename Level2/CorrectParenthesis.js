function solution(s){
    let stack = [];
    s = s.split('');
    for (let i=0; i<s.length; i++) {
        if (s[i] === '(') stack.push(s[i]);
        else if (s[i] === ')' && stack.pop() === undefined) {
            return false;
        }

    }
    return stack.length === 0;
}