import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(repr(node), "TextNode(This is a text node, bold, None)")

    def test_setURL(self):
        node = TextNode("URL node test", TextType.LINK, "www.url.com")
        self.assertEqual(node.url, "www.url.com")

    def test_noneURL(self):
        node = TextNode("URL node test", TextType.LINK)
        self.assertEqual(node.url, None)

if __name__ == "__main__":
    unittest.main()
