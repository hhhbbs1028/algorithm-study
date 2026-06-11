def solution(n, wires):
    # 송전탑 개수의 차이(절대값)
    # wires : [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
    answer = n
    for i in range(len(wires)):
        temp_wires = wires[:i] + wires[i+1:]
        nodes_a, nodes_b = set([wires[i][0]]), set([wires[i][1]])
        while len(nodes_a) + len(nodes_b) != n:
            for c, d in temp_wires:
                if c in nodes_a or d in nodes_a:
                    nodes_a.add(c)
                    nodes_a.add(d)
                elif c in nodes_b or d in nodes_b:
                    nodes_b.add(c)
                    nodes_b.add(d)
        answer = min(answer, abs(len(nodes_a) - len(nodes_b)))
    return answer