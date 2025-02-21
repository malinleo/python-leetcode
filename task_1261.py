from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"Val: {self.val}"

    def __repr__(self) -> str:
        return str(self)


class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        """Resolve contaminated tree to find elements."""
        self._initial = root or TreeNode(-1)
        self._initial.val = 0
        resolved = self._resolve_nodes_dfs(node=self._initial)
        self._bst = self._run_build_search_tree_dfs(node=resolved)

    def _resolve_nodes_dfs(self, node: TreeNode) -> TreeNode:
        if node.left:
            node.left = self._resolve_left_contaminated_node(
                parent_value=node.val,
                node=node.left,
            )
            node.left = self._resolve_nodes_dfs(node.left)
        if node.right:
            node.right = self._resolve_right_contaminated_node(
                parent_value=node.val,
                node=node.right,
            )
            node.right = self._resolve_nodes_dfs(node.right)
        return node

    def _to_array(self, node: TreeNode, nodes: list[int]) -> list[int]:
        if node.left:
            self._to_array(node.left, nodes)
        nodes.append(node.val)
        if node.right:
            self._to_array(node.right, nodes)
        return nodes

    def _build_search_tree(self, sorted_nodes: list[int]) -> TreeNode | None:
        if not sorted_nodes:
            return
        middle_idx = len(sorted_nodes) // 2
        return TreeNode(
            val=sorted_nodes[middle_idx],
            left=self._build_search_tree(sorted_nodes=sorted_nodes[:middle_idx]),
            right=self._build_search_tree(sorted_nodes=sorted_nodes[middle_idx + 1 :]),
        )

    def _run_build_search_tree_dfs(self, node: TreeNode) -> TreeNode | None:
        """."""
        nodes_array = self._to_array(node, [])
        nodes_array.sort()
        return self._build_search_tree(sorted_nodes=nodes_array)

    def _resolve_left_contaminated_node(
        self,
        parent_value: int,
        node: TreeNode,
    ) -> TreeNode:
        """Resolve left contaminated node by formula."""
        node.val = 2 * parent_value + 1
        return node

    def _resolve_right_contaminated_node(
        self,
        parent_value: int,
        node: TreeNode,
    ) -> TreeNode:
        """Resolve right contaminated node by formula."""
        node.val = 2 * parent_value + 2
        return node

    def find(self, target: int) -> bool:
        if not self._bst:
            return False
        return self._search_nodes_dfs(node=self._bst, target=target)

    def _search_nodes_dfs(self, node: TreeNode, target: int) -> bool:
        if self._check_node(node=node, target=target):
            return True

        if node.left:
            left_result = self._search_nodes_dfs(node.left, target=target)
        else:
            left_result = False

        if node.right:
            right_result = self._search_nodes_dfs(node.right, target=target)
        else:
            right_result = False
        return left_result or right_result

    def _check_node(self, node: TreeNode, target: int) -> bool:
        return node.val == target


if __name__ == "__main__":
    root = TreeNode(-1, right=TreeNode(-1))

    # Your FindElements object will be instantiated and called as such:
    obj = FindElements(root)
    target = 2
    param_1 = obj.find(target)
