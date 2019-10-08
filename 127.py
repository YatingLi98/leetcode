import collections
import queue


class Solution:
    graph = {}

    def ladderLength(self, beginWord, endWord, wordList):
        self.make_graph(wordList)
        start = self.first_transformed(beginWord, wordList)
        ans = [self.find_shortest(word, endWord) for word in start]
        return min(ans)

    def find_shortest(self, beginWord, endWord):
        q = queue.Queue()
        curr = beginWord
        visited = set()
        visited.add(beginWord)
        distance = dict()
        distance[beginWord] = 2
        while curr != endWord:
            keys = [curr[:i] + "*" + curr[i + 1:] for i in range(len(curr))]
            contain = []
            for k in keys:
                contain.extend(self.graph[k])
            for next_word in contain:
                if (next_word not in visited) and (curr != next_word):
                    distance[next_word] = distance[curr] + 1
                    visited.add(next_word)
                    q.put(next_word)
            if q.empty():
                return 0
            curr = q.get()
        return distance[curr]

    def first_transformed(self, begin, wordList):
        all = []
        for word in wordList:
            if self.one_different(word, begin):
                all.append(word)
        return all

    def one_different(self, w1, w2):
        if len(w1) != len(w2):
            return 0
        count = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                count += 1
            if count > 1:
                return 0
        return 1

    # def make_graph(self, wordList):
    #     self.graph = collections.defaultdict(list)
    #     for i in range(len(wordList)-1):
    #         for j in range(i+1, len(wordList)):
    #             if self.one_different(wordList[i], wordList[j]):
    #                 self.graph[wordList[i]].append(wordList[j])
    #                 self.graph[wordList[j]].append(wordList[i])
    def make_graph(self, wordList):
        self.graph = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                self.graph[word[:i] + "*" + word[i + 1:]].append(word)


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

s = Solution()
print(s.ladderLength(beginWord, endWord, wordList))
