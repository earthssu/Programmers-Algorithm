function solution(numbers, hand) {
    let answer = '';
    let lpos = '*';
    let rpos = '#';
    const phone = {1: [0,0], 2: [0,1], 3: [0,2], 4: [1,0], 5: [1,1], 6: [1,2], 7: [2,0], 8: [2,1], 9: [2,2], '*': [3,0], 0: [3,1], '#': [3,2]};
    numbers.forEach(item => {
        if (item === 1 || item === 4 || item === 7) {
            answer += 'L';
            lpos = item;
        }
        else if (item === 3 || item === 6 || item === 9) {
            answer += 'R';
            rpos = item;
        }
        else {
            let lLen = Math.abs(phone[item][0] - phone[lpos][0]) + Math.abs(phone[item][1] - phone[lpos][1]);
            let rLen = Math.abs(phone[item][0] - phone[rpos][0]) + Math.abs(phone[item][1] - phone[rpos][1]);
            if (lLen < rLen) {
                answer += 'L';
                lpos = item;
            }
            else if (rLen < lLen){
                answer += 'R';
                rpos = item;
            }
            else if (rLen === lLen) {
                if (hand === 'left') {
                    answer += 'L';
                    lpos = item;
                }
                else {
                    answer += 'R';
                    rpos = item;
                }
            }
        }
    })
    return answer;
}