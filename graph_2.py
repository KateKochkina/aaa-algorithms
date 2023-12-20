import pandas as pd
from collections import defaultdict, deque
from heapq import heappop, heappush


def dijkstra(graph, start, end):
    heap, seen_vertices, min_distances = [(0, start)], set(), {start: 0}
    steps = []
    while heap:
        curr_distance, current_vertex = heappop(heap)
        if current_vertex == end:
            return curr_distance
        if current_vertex not in seen_vertices:

            for next_vertex, distance in graph[current_vertex]:
                if next_vertex in seen_vertices:
                    continue

                prev_min_distance = min_distances.get(next_vertex)
                new_distance = curr_distance + distance

                if prev_min_distance is None or new_distance < prev_min_distance:
                    min_distances[next_vertex] = new_distance
                    heappush(heap, (new_distance, next_vertex))

            seen_vertices.add(current_vertex)

    return None


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
            dist = len(id_to_title[v_to])
            graph[v_from].append((v_to, dist))

    start = title_to_id["Analytics"]
    end = title_to_id["Algorithm"]
    res = dijkstra(graph, start, end)
    print(
        "Наименьшее (по сумме длин всех переходов) количество переходов по ссылкам равно",
        res,
    )
