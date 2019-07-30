# 如何实现反向DNS查找缓存
class TrieNode():
    def __init__(self):
        CHAR_COUNT = 11
        self.isLeaf = False
        self.url = None
        self.child = [None] * CHAR_COUNT
        i = 0
        while i < CHAR_COUNT:
            self.child[i] = None
            i += 1


def getIndexFromChar(c):
    return 10 if c == '.' else (ord(c) - ord('0'))

def getCharFromIndex(i):
    return '.' if i == 10 else ('0' + str(i))


class DNSCache():
    def __init__(self):
        self.CHAR_COUNT = 11
        self.root = TrieNode()

    def insert(self, ip, url):
        lens = len(ip)
        pCrawl = self.root
        level = 0
        while level < lens:
            index = getIndexFromChar(ip[level])
            if pCrawl.child[index] is None:
                pCrawl.child[index] = TrieNode()

            pCrawl = pCrawl.child[index]
            pCrawl.isLeaf = True
            pCrawl.url = url
            level += 1

    def searchDNSCache(self, ip):
        pCrawl = self.root
        lens = len(ip)
        level = 0
        while level < lens:
            index = getIndexFromChar(ip[level])
            if pCrawl.child[index] is None:
                return None
            pCrawl = pCrawl.child[index]
            level += 1

        if pCrawl is not None and pCrawl.isLeaf:
            return pCrawl.url

        return None


if __name__ == '__main__':
    ipAdds = ["10.57.11.127","121.57.61.129","66.125.100.103"]
    url = ["www.samsung.com","www.sansung.net","www.google.com"]
    n = len(ipAdds)
    cache = DNSCache()
    for i in range(n):
        cache.insert(ipAdds[i], url[i])
        i += 1

    ip = "121.57.61.129"
    res_url = cache.searchDNSCache(ip)
    if res_url is not None:
        print("对应的url为：", res_url)
    else:
        print("没有找到对应url")
