// C++ program to remove duplicates in-place
#include<iostream>
using namespace std;

int maximizeStockProfit(int stocks[], int n)
{
	if (n==0 || n==1)
		return n;

	int profit = 0, maxProfit = 0;

	for (int i=0; i < n-1; i++){
		if (stocks[i] < stocks[i+1]){
			profit = stocks[i + 1] - stocks[i];
			if(maxProfit < profit){
				maxProfit = maxProfit+profit;
			}	
		}
    }	
	return maxProfit;
}

// Driver code
int main()
{
	int stocks[] = {10, 7, 11, 8, 13, 2};
	int n = sizeof(stocks) / sizeof(stocks[0]);

	n = maximizeStockProfit(stocks, n);

	cout << n << " ";

	return 0;
}
