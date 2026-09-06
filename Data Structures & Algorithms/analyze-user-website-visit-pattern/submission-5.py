class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:

        logs = sorted(zip(timestamp, username, website))
        # need separation of websites by the username
        n = len(username)
        websites = defaultdict(list)
        for t, u, w in logs:
            websites[u].append(w)
        # need pattern counts of max length 3 of subsequences
        patterns = defaultdict(int)
        for name, list_website in websites.items():
            seen_patterns_for_user = set()
            # generate all patterns (as subsequences) for this user
            for i in range(len(list_website)):
                for j in range(i+1, len(list_website)):
                    for k in range(j+1, len(list_website)):
                        pattern = (list_website[i], list_website[j], list_website[k])
                        if pattern not in seen_patterns_for_user:
                            patterns[pattern] += 1
                            seen_patterns_for_user.add(pattern)
        # print(patterns)
        max_count = 0
        max_pattern = None
        # iterate through patterns and get the max count of one with lexicographically small
        for pattern, count in patterns.items():
            # print(pattern, count, max_pattern, max_count)
            if count > max_count:
                max_count = count
                max_pattern = pattern
            elif count == max_count and pattern < max_pattern:
                max_pattern = pattern
        return list(max_pattern)