#递归的深度优先搜索
def rec_dfs(G,s,S=None):
    if S is None:S = set()
    S.add(s)
    for u in G[s]:
        if u in S: continue
        rec_dfs(G,u,S)
        return u

#迭代的深度优先搜索
def iter_dfs(G,s):
    S,Q=set(),[]
    Q.append(s)
    while Q:
        u = Q.pop()
        if u in S:continue
        S.add(u)
        Q.extend(G[u])
        yield u

if __name__ == "__main__":
    a, b, c, d, e, f, g, h, i = range(9)
    G = [{b, c, d, e, f},  # a
         {c, e},           # b
         {d},              # c
         {e},              # d
         {f},              # e
         {c, g, h},        # f
         {f, h},           # g
         {f, g}            # h
              ]
    print(list(iter_dfs(G,a)))       # [0, 5, 7, 6, 2, 3, 4, 1]