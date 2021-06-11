#include <iostream>

using namespace std;

void test_case() {

}

int main() {
    // read number of cases
    int num_cases;
    scanf("%d", &num_cases);

    // read individual case and solve
    for (int case_id = 1; case_id <= num_cases; case_id++) {
        printf("Case %d:", case_id);
        test_case();
    }
}
