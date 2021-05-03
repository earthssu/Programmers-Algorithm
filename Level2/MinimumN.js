function solution(arr) {
    let max = Math.max(...arr);
    let answer = max;
    while (max) {
        let truth = true;
        for (let i=0; i<arr.length; i++) {
            if (answer % arr[i] !== 0) {
                truth = false;
                break;
            }
        }
        if (truth === true) return answer;
        else answer += max;
    }
}