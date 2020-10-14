#Uses python3

def build_trie(patterns):
    trie={}
    trie[0]={}
    index=1
    for pattern in patterns:
        curr_node=trie[0]
        for letter in pattern:
            # print("Currently Processing",letter)
            if letter in curr_node.keys(): # if letter is in current paths outgoing from current node
                # print(letter,"already there")
                curr_node=trie[curr_node[letter]] # then propogate to it, i.e next root
                # print("current node",curr_node)
            else:
                # print("Adding new node")
                curr_node[letter]=index
                trie[index]={}
                curr_node=trie[index]
                # print("current node",curr_node)
                index+=1

    return trie

def prefix_trie_matching(text,trie):
	index=0
	symbol=text[index]
	# print(text)
	current=trie[0]
	while True:
		if not current: # there is node in this trie
			return True
		elif symbol in current.keys(): # there is link from this to another
			current=trie[current[symbol]] # move to that node
			index=index+1
			if index<len(text):
				symbol=text[index]
			else:
				symbol='-'
		else:
			return False





def solve (text, n, patterns):
	result = []
	trie=build_trie(patterns)
	n=len(text)
	for i in range(n):
		if prefix_trie_matching(text[i:],trie):
			result.append(i)
	return result

text=input()
n = int(input())
patterns= []
for _ in range(n):
	patterns.append(input())

ans = solve (text, n, patterns)
print(*ans)
# sys.stdout.write (' '.join (map (str, ans)) + '\n')
