class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # . is ignored
        # + ignores all afterwards

        # split email into local and domain name
        email_map = defaultdict(set)
        count = 0
        # parse each local and domain name, add to hashmap with {local name: domain name}
        for email in emails:
            email_splitted = email.split("@")
            local, domain = email_splitted[0], email_splitted[1]
            
            # local = "".join(local.split('.'))
            local = local.replace('.', '')
            local = local.split('+')[0]
            
            # domain = "".join(domain.split('.'))
            email_map[domain].add(local)
        # print(email_map)
        # return the number of unique keys of the hashmap
        for _, sett in email_map.items():
            count += len(sett)
        return count