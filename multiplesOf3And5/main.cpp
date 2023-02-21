auto solution(int number) -> int {
    int sum = 0;
    for(int i = 1; i < number; i++) {
        if (i % 3 == 0 || i % 5 == 0) {
            sum += i;
        }
    }
    return sum;
}
