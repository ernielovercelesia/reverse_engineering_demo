#include <stdio.h>
#include <string.h>

int main() {
    char key[20];
    printf("Enter license key: ");
    scanf("%19s", key);

    if (strcmp(key, "license12345") == 0) {
        printf("Access granted!\n");
    } else {
        printf("Access denied!\n");
    }
    return 0;
}
