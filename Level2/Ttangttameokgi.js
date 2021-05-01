function solution(land) {
    const len = land.length;

    for (let i = 1; i < len; i++) {
        for (let j = 0; j < 4; j++) {
            let landArr = land[i - 1].slice();
            landArr.splice(j, 1);
            land[i][j] += Math.max(...landArr);
        }

    }
    return Math.max(...land[len - 1]);
}