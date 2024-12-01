#include <stdio.h>
#include <stdlib.h>

typedef struct {
        int size;
        int capacity;
        int *data;
} Array;

int init_array(Array *arr) {
        arr->size = 0;
        arr->capacity = 0;
        arr->data = (int *)malloc(0);

        if (arr->data == NULL) {
                printf("Could not initialize array\n");
                return 1;
        }

        return 0;
}

int add_to_array(Array *arr, int value) {
        // Increase size of array
        if (arr->size + 2 > arr->capacity) {
                arr->capacity = arr->capacity == 0 ? 1 : arr->capacity * 2;
                int *data = realloc(arr->data, arr->capacity * sizeof(int));
                if (data == NULL) {
                        printf("Memory allocation failed.\n");
                        free(data);
                        return 1;
                }
                arr->data = data;
        }

        arr->data[arr->size++] = value;

        return 0;
}

int compare(const void *a, const void *b) {
        int *left = (int *)a;
        int *right = (int *)b;

        if (*left < *right) {
                return -1;
        } else if (*left > *right) {
                return 1;
        } else {
                return 0;
        }
}

int main() {
        Array left_arr;
        Array right_arr;
        if (init_array(&left_arr) != 0) {
                printf("Error: can't initialize array.\n");
                return 1;
        }

        if (init_array(&right_arr) != 0) {
                printf("Error: can't initialize array.\n");
                return 1;
        }

        FILE *fp = fopen("input.txt", "r");
        if (fp == NULL) {
                printf("Error: can't open file");
                return 1;
        }

        int result_part1 = 0;
        int left, right;

        while (fscanf(fp, "%d   %d", &left, &right) == 2) {
                add_to_array(&left_arr, left);
                add_to_array(&right_arr, right);
        }

        qsort(left_arr.data, left_arr.size, sizeof(int), compare);
        qsort(right_arr.data, right_arr.size, sizeof(int), compare);

        for (int i = 0; i < left_arr.size; i++) {
                result_part1 += abs(left_arr.data[i] - right_arr.data[i]);
        }

        int result_part2 = 0;
        int right_index = 0;
        for (int i = 0; i < left_arr.size; i++) {
                while (right_arr.data[right_index] < left_arr.data[i]) {
                        right_index++;
                }

                while (right_arr.data[right_index] == left_arr.data[i]) {
                        result_part2 += left_arr.data[i];
                        right_index++;
                }
        }

        printf("Results:\n");
        printf("\tpart 1: %d\n", result_part1);
        printf("\tpart 2: %d\n", result_part2);
        return 0;
}