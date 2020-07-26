#Uses python3

def build_trie(patterns):
    trie = {}
    trie[0] = {}
    index = 1

    for pattern in patterns:
        curr_node = trie[0]
        for letter in pattern:
            if letter in curr_node.keys():  #if the alphabet is there in the Current paths emanating from Current node
                curr_node = trie[curr_node[letter]] #move to the next root node
            else:
                curr_node[letter] = index # adding node number to this letter, ex 0: {'a': 1} means 0-1 edge is a
                trie[index] = {} # creating dictionary for letters to follow the Current letter, ex: creating 1:{} so we can store  1-somenode
                #                 where some alphabet  is on edge 1-somenode
                curr_node = trie[index]  #shifting to the newly created node
                index = index + 1
        curr_node['$'] = {} #adding a dollar symbol at the end
    return trie

def prefix_trie_matching(text,trie,external_index):
	index=0
	symbol=text[index]
	# print(text)
	current=trie[0]
	res=-1 # Default result
	while True:
		if (not current) or ('$' in current) : # there is node in this trie
			return res
		if symbol in current: # there is link from this to next level
			current=trie[current[symbol]] # move to that node
			res=external_index
			index=index+1
			if index<len(text):
				symbol=text[index]
			elif '$' in current:
				return res
			else:
				symbol='@'
				res=-1
		else:
			return res if '$' in current else -1





def solve (text, n, patterns):
	result = []
	trie=build_trie(patterns)
	n=len(text)
	for i in range(n):
		if prefix_trie_matching(text[i:],trie,i)!=-1:
			result.append(prefix_trie_matching(text[i:],trie,i))
	return sorted(list(result))

text=input()
n = int(input())
patterns= []
for _ in range(n):
	patterns.append(input())

ans = solve (text, n, patterns)
print(*ans)

