int persistence(long long n){
    int count {0}; 
    while(n > 9) {
        count++;
        int tmp = 1;
        while(n != 0) {
            tmp *= n % 10;
            n /= 10;
        }

        n = tmp;
    }

    return count;
}
