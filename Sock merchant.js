function sockMerchant(n, ar) {
    let pairs = 0;
    const obj = {};
    ar.forEach(i => {
        if (obj[i]) {
            pairs += 1;
            obj[i] = 0;
        } else {
            obj[i] = 1;
        }
    });
    return pairs;

}