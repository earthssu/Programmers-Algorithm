function solution(info, query) {
    let answer = [];
    let info_obj = {};

    info.forEach((i) => {
        i = i.split(' ');
        const i_key = i.slice(0, 4);
        const i_val = parseInt(i[4], 10);
        for (let k=0;k<5;k++) {
            combination(i_key, k).forEach((c) => {
                const tmp_c = c.join('');
                if (tmp_c in info_obj) info_obj[tmp_c].push(i_val);
                else info_obj[tmp_c] = [i_val];
            })
        }
    })

    for (const [key, value] of Object.entries(info_obj)) {
        value.sort((a,b)=>a-b);
    }

    query.forEach((q) => {
        q = q.split(' ');
        const q_score = parseInt(q[7], 10);
        q = q.slice(0, 7);
        q = q.filter((str) => str !== 'and');
        q = q.filter((str) => str !== '-');

        const tmp_q = q.join('');
        if (tmp_q in info_obj) {
            const scores = info_obj[tmp_q];
            if (scores.length > 0) {
                let start = 0;
                let end = scores.length;
                while (end > start) {
                    let mid = Math.floor((start+end)/2);
                    if (scores[mid] >= q_score) {
                        end = mid;
                    }
                    else {
                        start = mid + 1;
                    }
                }
                answer.push(scores.length - start);
            }
        }
        else answer.push(0);
    })

    return answer;
}

const combination = (arr, num) => {
    const result = [];
    if (num === 1) return arr.map((v) => [v]);
    if (num === 0) return [[]];
    arr.forEach((v, idx, arr) => {
        const fixed = v;
        const restArr = arr.slice(idx + 1);
        const combinationArr = combination(restArr, num -1);
        const combineFix = combinationArr.map((v) => [fixed, ...v]);
        result.push(...combineFix);
    })
    return result;
}


console.log(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]));