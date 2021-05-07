function solution(n, works) {
    let max = works.sort((a,b)=> b-a)[0];
    while (n > 0) {
        for (let i=0; i<works.length; i++) {
            if (max === works[i]) {
                works[i] -= works[i] > 0 ? 1 : 0;
                n--;
            }
            if(!n) break;
        }
        max--;
        if (!max) break;
    }
    return works.reduce((sum, curValue) => {
        if (curValue > 0) curValue = curValue ** 2;
        return sum + curValue;
    }, 0);
}