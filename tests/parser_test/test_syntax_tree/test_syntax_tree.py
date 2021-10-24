import unittest

from src.ufu_parser.syntax_tree import SyntaxTree, SyntaxNode

from src.tree_graphviz_visualizer import TreeGraphvizVisualizer


class SyntaxTreeCase(unittest.TestCase):

    def test_insert_node(self):
        root_name = 'root'
        tree = SyntaxTree(SyntaxNode(root_name))

        self.assertEqual(tree.root.name, root_name)

        tree.insert_node_in_parent(SyntaxNode('n1'))
        tree.insert_node_in_parent(SyntaxNode('n2'))
        tree.insert_node_in_parent(SyntaxNode('n3'))

        self.assertEqual(len(tree.root.children), 3)
        self.assertEqual(len(tree.parent.children), 3)

        new_parent = SyntaxNode('n4')
        tree.insert_new_parent(new_parent)

        self.assertEqual(len(tree.root.children), 4)
        self.assertEqual(len(tree.parent.children), 0)

        self.assertNotEqual(tree.root, tree.parent)

        tree.insert_node_in_parent(SyntaxNode('n5'))

        self.assertEqual(len(tree.parent.children), 1)

        tree.insert_new_parent(SyntaxNode('n6'))
        tree.insert_node_in_parent(SyntaxNode('n8'))

        visualizer = TreeGraphvizVisualizer()

        content_file = visualizer.generate_graphviz_file(tree.root)

        with open('tests/assets/dot_files/tree.dot', 'w') as file:
            file.write(content_file)
