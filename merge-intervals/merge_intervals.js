/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function(intervals) {
	if (intervals.length == 0) {
		return []
	}
	if (intervals.length == 1) {
		return intervals
	}

	let ans = []
	intervals = intervals.sort(function(a, b) {
		return a[0] - b[0];
	});
	ans.push(intervals[0]);
	for (let i = 1; i <= intervals.length - 1; i++) {
		if (ans[ans.length - 1][1] >= intervals[i][0]) {
			if (ans[ans.length - 1][1] <= intervals[i][1]) {
                ans[ans.length - 1][1] = intervals[i][1]
			} 
		} else {
			ans.push(intervals[i])
		}
	}
	return ans;
};
