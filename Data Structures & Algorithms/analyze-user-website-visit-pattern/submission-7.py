class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        # sort by timestamp
        items = sorted(zip(timestamp, username, website))
        # get a hashmap of list by username
        map_webs = defaultdict(list)
        for _, u, w in items:
            map_webs[u].append(w)
        # get all subsequences from the list and store as hashmap with count
        web_counter = defaultdict(int)
        for name, webs in map_webs.items():
            visited = set()
            for i in range(len(webs)):
                for j in range(i+1, len(webs)):
                    for k in range(j+1, len(webs)):
                        subseq = tuple([webs[i], webs[j], webs[k]])
                        if subseq not in visited:
                            visited.add(subseq)
                            web_counter[subseq] += 1
        # get the lexicographically smallest of the largest pattern score
        max_pattern = None
        max_count = 0
        # print(web_counter)
        for pattern, count in web_counter.items():
            # print(pattern, count, max_pattern, max_count)
            if max_count < count:
                max_pattern = pattern
                max_count = count
            elif max_count == count:
                if pattern < max_pattern:
                    max_pattern = pattern
        return list(max_pattern)