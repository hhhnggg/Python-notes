#include <iostream>

using namespace std;

void array_add(int* p, int n)
{
    for (int i = 0; i < n; i++)
    {
        *p = *p + 30;
        p++;
    }
}

int main(void)
{
    int a[10];
    
    for (int i = 0; i < 10; i++)
    {
        a[i] = i;
    }
    
    array_add(&a[5], 2);
    
    for (int i = 0; i < 10; i++)
    {
        printf("%d ", a[i]);
    }

    return 0;
}
