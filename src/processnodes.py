from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    '''
    takes a list of "old nodes", a delimiter, and a text type. 
    returns a new list of nodes, where:
        any "text" type nodes in the input list are (potentially) split into 
        multiple nodes based on the syntax. For example, given the following input:

        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        new_nodes becomes:

        [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
    '''
    retlist = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            retlist.append(node)
        else:
            count = 0
            for subnode in node.text.split(delimiter):
                count += 1
                if count % 2 == 0:
                    retlist.append(TextNode(subnode, text_type))
                elif len(subnode) > 0:
                    retlist.append(TextNode(subnode, TextType.TEXT))
    return retlist




            





