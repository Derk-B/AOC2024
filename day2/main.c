#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define MAX_LINE_LENGTH 64

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

int remove_from_array(Array *arr, int position) {
    int *new_data = (int *)malloc(arr->capacity);

    int p = 0;
    for (int i = 0; i <= arr->size; i++) {
        if (i == position) continue;

        new_data[p] = arr->data[i];
        printf("kept: %d\n", new_data[p]);
    }

    arr->data = new_data;

    return 0;
}

int copy_array_except(Array *src, Array *dest, int skip_index) {
    for (int i = 0; i < src->size; i++) {
        if (i == skip_index) continue;
        add_to_array(dest, src->data[i]);
    }
    return 0;
}

bool is_valid_increasing(int a, int b) { return a < b && ((b - a) <= 3); }
bool is_valid_decreasing(int a, int b) { return b < a && ((a - b) <= 3); }

int is_increasing(Array arr, int *index1, int *index2) {
    for (int i = 1; i < arr.size - 1; i++) {
        int prev = arr.data[i - 1];
        int curr = arr.data[i];
        int next = arr.data[i + 1];

        if (is_valid_increasing(prev, curr)) continue;

        *index1 = i;
        *index2 = i - 1;
        return false;
    }

    if (!is_valid_increasing(arr.data[0], arr.data[1])) {
        *index1 = 0;
        return false;
    }

    if (!is_valid_increasing(arr.data[arr.size - 2], arr.data[arr.size - 1])) {
        *index1 = arr.size - 1;
        return false;
    }

    return true;
}

int is_decreasing(Array arr, int *index1, int *index2) {
    for (int i = 1; i < arr.size - 1; i++) {
        int prev = arr.data[i - 1];
        int curr = arr.data[i];
        int next = arr.data[i + 1];

        if (is_valid_decreasing(prev, curr)) continue;

        *index1 = i;
        *index2 = i - 1;
        return false;
    }

    if (!is_valid_decreasing(arr.data[0], arr.data[1])) {
        *index1 = 0;
        return false;
    }

    if (!is_valid_decreasing(arr.data[arr.size - 2], arr.data[arr.size - 1])) {
        *index1 = arr.size - 1;
        return false;
    }

    return true;
}

int main() {
    Array arr;
    if (init_array(&arr) != 0) {
        printf("Error: can't initialize array.\n");
        return 1;
    }

    FILE *fp = fopen("input.txt", "r");
    if (fp == NULL) {
        printf("Error: can't open file");
        return 1;
    }

    int result_part1 = 0;
    int result_part2 = 0;
    char *line;
    size_t len = 0;
    ssize_t read;
    char *token;
    const char delim[1] = " ";

    while ((read = getline(&line, &len, fp)) != -1) {
        char *token = strtok(line, delim);

        while (token != 0) {
            int number;
            if (sscanf(token, "%d", &number) != 0) {
                add_to_array(&arr, number);
            }

            token = strtok(0, delim);
        }

        int inc_violation_index1, inc_violation_index2, dec_violation_index1,
            dec_violation_index2;
        bool inc =
            is_increasing(arr, &inc_violation_index1, &inc_violation_index2);
        bool dec =
            is_decreasing(arr, &dec_violation_index1, &dec_violation_index2);
        if (inc || dec) {
            result_part1++;
            result_part2++;
            init_array(&arr);
            continue;
        }

        Array inc_array1, inc_array2, dec_array1, dec_array2;
        init_array(&inc_array1);
        init_array(&dec_array1);
        init_array(&inc_array2);
        init_array(&dec_array2);

        copy_array_except(&arr, &inc_array1, inc_violation_index1);
        copy_array_except(&arr, &dec_array1, dec_violation_index1);
        copy_array_except(&arr, &inc_array2, inc_violation_index2);
        copy_array_except(&arr, &dec_array2, dec_violation_index2);

        int _out;
        if (is_increasing(inc_array1, &_out, &_out) ||
            is_decreasing(dec_array1, &_out, &_out) ||
            is_increasing(inc_array2, &_out, &_out) ||
            is_decreasing(dec_array2, &_out, &_out)) {
            result_part2++;
        }

        free(inc_array1.data);
        free(dec_array1.data);

        free(inc_array2.data);
        free(dec_array2.data);
        init_array(&arr);
    }

    printf("Results:\n");
    printf("\tpart 1: %d\n", result_part1);
    printf("\tpart 2: %d\n", result_part2);
    return 0;
}
