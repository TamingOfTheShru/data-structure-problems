# Input : abcd
# Output : abcd abc ab a bcd bc b cd c d - 10
# All Elements are Distinct
#
# Input : aaa
# Output : aaa aa a aa a a
# All elements are not Distinct


def distinct_substrings(str) -> int:
    if len(s) == 0:
        return None
    result = set()
    for i in range(0, len(s)+1):
        for j in range(i+i, len(s)+1):
            result.add(s[i:j])
    return len(result)+1


print(distinct_substrings("abcd"))
