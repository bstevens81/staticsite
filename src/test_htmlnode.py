import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_create_1(self):
        testNode = HTMLNode("a","value")
        self.assertEqual(testNode.tag, "a")
        self.assertEqual(testNode.value, "value")

    def test_create_2(self):
        testNodeChild1 = HTMLNode("a", "value")
        testNodeChild2 = HTMLNode("b", "2alue")
        children = [testNodeChild1, testNodeChild2]

        testNode = HTMLNode(children = children)

        self.assertIn("a", str(testNode))
        self.assertIn("b", str(testNode))
        self.assertIn("value", str(testNode))
        self.assertIn("2alue", str(testNode))

    def test_props_to_html_1(self):
        testNode = HTMLNode(props = \
                {
                    "href": "https://www.google.com",
                    "target": "_blank",
                }
                )
        self.assertEqual(testNode.props_to_html(),
                        ' href="https://www.google.com" target="_blank"')

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")


    def test_leaf_to_html_b(self):
        node = LeafNode("b", "Hello, world!")
        self.assertEqual(node.to_html(), "<b>Hello, world!</b>")

    def test_leaf_to_html_href(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')


