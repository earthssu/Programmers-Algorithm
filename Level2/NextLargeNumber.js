function solution(n) {
    let largeNum = n + 1;
    const count = (n.toString(2)).match(/1/g).length;
    while (largeNum > 1) {
        if (count === largeNum.toString(2).match(/1/g).length) return largeNum;
        largeNum += 1
    }
}