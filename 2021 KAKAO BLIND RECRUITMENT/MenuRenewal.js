function solution(orders, course) {
    let answer = [];
    orders = orders.map(e=>e.split('').sort().join(''));

    course.forEach((num) => {
        let order_obj = {};
        orders.forEach((order) => {
            order = order.split('');
            combination(order, num).forEach((c) => {
                const tmp_c = c.join('');
                if (tmp_c in order_obj) {order_obj[tmp_c] += 1;}
                else {order_obj[tmp_c] = 1;}
            })
        })
        let max_num = 0;
        let menu = '';
        for (menu in order_obj) {
            if (order_obj[menu] > max_num) {
                max_num = order_obj[menu];
            }
        }
        for (menu in order_obj) {
            if (order_obj[menu] === max_num && max_num > 1) {
                answer.push(menu);
            }
        }
    })

    return answer.sort();
}


const combination = (arr, num) => {
    const result = [];
    if (num === 1) return arr.map((v) => [v]);
    arr.forEach((v, idx, arr) => {
        const fixed = v;
        const restArr = arr.slice(idx + 1);
        const combinationArr = combination(restArr, num -1);
        const combineFix = combinationArr.map((v) => [fixed, ...v]);
        result.push(...combineFix);
    })
    return result;
}