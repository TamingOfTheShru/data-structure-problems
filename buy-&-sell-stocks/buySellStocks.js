/**
 * 	Say you have an array for which the ith element is the price of a given stock on day i.
 *	Design an algorithm to find the maximum profit. You may complete as many transactions as you like 
 * 	(ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple 
 *  transactions at the same time (ie, you must sell the stock before you buy again).
 */
var stocks = [10, 7, 11, 8, 13, 2];

function maximizeStockProfit(stocks) {
	if (stocks === null || stocks.length === 0) return 0;
	if (stocks.length == 1) return 1;
	var profit, maxProfit = 0;
	for (var i = 0; i < stocks.length; i++) {
		if (stocks[i] < stocks[i + 1]) {
			profit = stocks[i + 1] - stocks[i];
			if (maxProfit < profit) {
				maxProfit = maxProfit + profit;
			}
		}
	}
	console.log(maxProfit);
	return maxProfit;
};

maximizeStockProfit(stocks);