from typing import List, Set, Self, Dict


class GridNode:

    def __init__(self, id: int, connections: Set[Self]) -> None:
        self.id = id
        self.connections = connections
        self.is_active = True

    def deactivate(self):
        self.is_active = False

    def traverse(self, seen_ids: Set[int]) -> Set[Self]:
        nodes = self.connections.copy()
        for node in nodes:
            new_nodes = node.traverse(seen_ids)
            if self not in seen_ids:
                nodes.update(new_nodes)
        return nodes

    def __hash__(self) -> int:
        return self.id


class Grid:

    def __init__(self, nodes: List[GridNode], lowest_id: int) -> None:
        self._nodes = nodes
        self._lowest_id = lowest_id

    @classmethod
    def from_connections(cls, c: int, connections: List[List[int]]) -> Dict[int, Self]:
        # 1. Build all possible grids
        # 2. Map each station id to grid where it is located
        station_to_grid_map = {}
        node_connections: Dict[int, Set[int]] = {}
        nodes = []
        for connection in connections:
            node_connections.setdefault(connection[0], set())
            node_connections[connection[0]].add(connection[1])

        for i in range(1, c + 1):
            curr_node_conns = node_connections.get(i, set())
            nodes.append(GridNode(i, curr_node_conns))

        while nodes:
            curr_lowest_node = nodes.pop(0)

            new_grid = Grid()
        return {c: cls()}

    def _traverse_nodes()

    def check(self, node_id: int) -> int: ...

    def deactivate(self, node_id: int) -> None: ...


class Solution:
    def processQueries(
        self, c: int, connections: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        station_to_grid_map = Grid.from_connections(c, connections)
        result = []
        for query in queries:
            station_id = query[1]
            if query[0] == 1:
                grid = station_to_grid_map[station_id]
                result.append(grid.check(station_id))
            else:
                grid.deactivate(station_id)
        return result
