const floydWarshall = (dist) => {
    const len = dist.length;
    for (let i=0; i<len; i++) { // 거쳐야 할 정점
        for (let j=0; j<len; j++) { // 시작 정점
            for (let k=0; k<len; k++) { // 인접 정점
                if (dist[j][k] > dist[j][i] + dist[i][k]) {
                    dist[j][k] = dist[j][i] + dist[i][k];
                }
            }
        }
    }
}