"""
A website domain "discuss.leetcode.com" consists of various subdomains. At the top level, we have "com", at the next level, we have "leetcode.com" and at the lowest level, "discuss.leetcode.com". When we visit a domain like "discuss.leetcode.com", we will also visit the parent domains "leetcode.com" and "com" implicitly.

A count-paired domain is a domain that has one of the two formats "rep d1.d2.d3" or "rep d1.d2" where rep is the number of visits to the domain and d1.d2.d3 is the domain itself.

    For example, "9001 discuss.leetcode.com" is a count-paired domain that indicates that discuss.leetcode.com was visited 9001 times.

Given an array of count-paired domains cpdomains, return an array of the count-paired domains of each subdomain in the input. You may return the answer in any order.
"""

from collections import defaultdict

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        wtf = defaultdict(int)

        def get_domain_names(domain):
            parts = domain.split('.')
            domains = []
            for i in range(len(parts)):
                domains.append('.'.join(parts[i:]))
            return domains

        for row in cpdomains:
            count, domain = row.split(' ')
            count = int(count)
            domain_names = get_domain_names(domain)
            for domain_name in domain_names:
                wtf[domain_name] += count

        ans = []
        for key, val in wtf.items():
            ans.append("%d %s" % (val, key))
        return ans