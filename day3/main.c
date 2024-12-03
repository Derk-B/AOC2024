#include <regex.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

bool starts_with(const char *str, const char *prefix, size_t prefix_len) {
    const char *ptr = str;

    if (strncmp(ptr, prefix, prefix_len) == 0) return true;
    return false;
}

int find_multiplication(const char *str) {
    const char *ptr = str;
    const char *prefix = "mul";
    const int prefix_len = strlen(prefix);

    // Check if string starts with "mul("
    if (!starts_with(ptr, prefix, prefix_len)) return 0;

    ptr += prefix_len;

    int n1, n2;
    char open, comma, close;

    if (sscanf(ptr, "%c%d%c%d%c", &open, &n1, &comma, &n2, &close) == 5) {
        if (open == '(' && comma == ',' && close == ')') {
            return n1 * n2;
        }
    }

    return 0;
}

int main() {
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

    bool enabled = true;
    while ((read = getline(&line, &len, fp)) != -1) {
        char *line_copy = line;
        while (*line_copy != '\0') {
            if (starts_with(line_copy, "don't()", strlen("don't()"))) {
                enabled = false;
            } else if (starts_with(line_copy, "do()", strlen("do()"))) {
                enabled = true;
            }
            int _res = find_multiplication(line_copy);

            result_part1 += _res;
            if (enabled) result_part2 += _res;

            line_copy++;
        }
    }

    printf("Results:\n");
    printf("\tpart 1: %d\n", result_part1);
    printf("\tpart 2: %d\n", result_part2);
    return 0;
}
