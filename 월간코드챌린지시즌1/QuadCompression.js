function quad(array, size, countArray, start) {
    const first = array[start[0]][start[1]];
    if (size === 1) {
        first === 0 ? countArray[0] += 1 : countArray[1] += 1;
        return;
    }

    const half = size / 2;
    let keep = true;

    for (let i=start[0]; i<start[0]+size; i++) {
        for (let j=start[1]; j<start[1]+size; j++) {
            if (first !== array[i][j]) {
                keep = false;
                break;
            }
        }
        if (!keep) break;
    }

    if (keep) {
        first === 0 ? countArray[0]++ : countArray[1]++;
        return;
    }

    quad(array, half, countArray, start);
    quad(array, half, countArray, [start[0], start[1]+half]);
    quad(array, half, countArray, [start[0]+half, start[1]]);
    quad(array, half, countArray, [start[0]+half, start[1]+half]);
    return;
}

function solution(arr) {
    const answer = [0, 0];
    const size = arr.length;
    quad(arr, size, answer, [0, 0]);
    return answer;
}