#Uses python3
import sys

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.
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

n = int(input())
patterns= []
for _ in range(n):
    patterns.append(input())

tree = build_trie(patterns)
for node in tree:
    for c in tree[node]:
        print("{}->{}:{}".format(node, tree[node][c], c))
