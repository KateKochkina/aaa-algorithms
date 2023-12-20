import pandas as pd
from collections import defaultdict, deque


def bfs(start: int, end: int, graph: dict[int, list]) -> int:
    visited = {start}
    shortest_dist, shortest_paths = None, []
    queue = deque([(start, 0, [start])])
    while queue:
        v_cur, dist, path = queue.popleft()
        if v_cur == end:
            if shortest_dist is None:
                shortest_dist = dist
            if dist == shortest_dist:
                shortest_paths.append(path)
            else:
                return shortest_paths
        for v_next, _ in graph[v_cur]:
            if v_next not in visited:
                visited.add(v_next)
                queue.append((v_next, dist + 1, path + [v_next]))
    return shortest_paths


if __name__ == "__main__":

    id_to_title = {}
    title_to_id = {}

    df = pd.read_csv("simple_english_wiki_pages.csv")

    for _, row in df.iterrows():
        id = row["page_id"]
        title = row["page_title"]
        id_to_title[id] = title
        title_to_id[title] = id

    graph = defaultdict(list)

    with open("simple_english_wiki_pagelinks.csv", "r") as f_in:
        f_in.readline()
        for line in f_in:
            elems = line.strip().split(",")
            v_from = int(elems[0])
            v_to = int(elems[-1])
            graph[v_from].append((v_to, dist))

    start = title_to_id["Analytics"]
    end = title_to_id["Algorithm"]
    res = bfs(start, end, graph)
    print("Наименьшее количество переходов по ссылкам равно", len(res[0]) - 1)
    print(
        "На кратчайшем пути ссылку на статью Algorithm содержит статья:",
        id_to_title[res[0][-2]],
    )
