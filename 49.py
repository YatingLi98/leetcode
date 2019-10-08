import collections


def groupAnagrams(strs):
    group = collections.defaultdict(list)
    for str in strs:
        key = tuple(ch for ch in sorted(str))
        group[key].append(str)
    return [group.get(k) for k in group]


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
