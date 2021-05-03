function solution(s) {
    const sArr = s.toLowerCase().split(" ").map(str => {
        if (str.match(/^[^0-9]/)) {
            str = str.charAt(0).toUpperCase() + str.slice(1);
        }
        return str;
    })
    return sArr.join(' ');
}