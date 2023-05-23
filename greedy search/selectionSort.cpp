#include <bits/stdc++.h>
#include <iostream>
using namespace std;

void selectionSort(vector<int> &arr, int n)
{
    for (int i = 0; i < n - 1; i++)
    {
        int minIdx = i;
        for (int j = i + 1; j < n; j++)
        {
            if (arr[j] < arr[minIdx])
            {
                minIdx = j;
            }
        }
        swap(arr[minIdx], arr[i]);
    }
}

int main()
{
    vector<int> arr(5);

    cout << "Enter the numbers:";
    for (int i = 0; i < arr.size(); i++)
    {
        cin >> arr[i];
    }

    int size = arr.size();

    selectionSort(arr, size);

    for (int i = 0; i < size; i++)
    {
        cout << arr[i] << " ";
    }
}