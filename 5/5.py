from typing import List

class Solution:
    def max_destroyed_roads(self, graph: List[List[int]]):
        def find_components() -> int:
            components = [0 for _ in range(cities_count)]
            def dfs(v: int, c_num: int):
                components[v] = c_num
                for u in range(cities_count):
                    if components[u] == 0 and graph[v][u]:
                        dfs(u, c_num)

            c_num = 1
            for i in range(cities_count):
                if components[i] == 0:
                    dfs(i, c_num)
                    c_num += 1
            return components[-1]

        def remove_roads(y: int) -> None:
            for i in range(cities_count):
                for j in range(cities_count):
                    graph[i][j] = list(filter(lambda x: x > y, graph[i][j]))

        components_count = find_components()
        x = 1
  
        while components_count == find_components():
            remove_roads(x)
            x += 1
        return x - 2

cities_count, roads_count = map(int, input().split(' '))
graph = [ [ [] for _2 in range(cities_count) ] for _1 in range(cities_count) ]

for _ in range(roads_count):
    first_city, second_city, road = map(int, input().split(' '))
    graph[first_city - 1][second_city - 1].append(road)
    graph[second_city - 1][first_city - 1].append(road)

solution = Solution()
print(solution.max_destroyed_roads(graph))
