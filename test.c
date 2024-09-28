#include <stdio.h>

int findMax(int A[], int N) {
    if (N <= 1) {
        return A[0];
    } else {
        int maxValue = findMax(A, N - 1);
        if (A[N - 1] > maxValue) {
            return A[N - 1];
        } else {
            return maxValue;
        }
    }
}

int main() {
    int A[] = {0, -2, 3, 4, 0, 6};
    int N = 6;
    int maxValue = findMax(A, N);
    printf("Maximum value in the array is %d\n", maxValue);
    return 0;
}