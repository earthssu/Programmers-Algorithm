function solution(s) {
    let numArr = s.split(' ');
    return Math.min(...numArr) + " " + Math.max(...numArr);
}