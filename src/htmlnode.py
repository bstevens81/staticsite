

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag #A string representing the HTML tag name ("p","a","h1")
        self.value = value #A string representing the value of the HTML tag (eg, text inside para)
        self.children = children #A list of HTMLNode objects representing children of the node
        self.props = props #A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}

    def __repr__(self):
        return ' '.join(['Tag:', str(self.tag), '\nValue:', str(self.value), '\nChildren:', str(self.children),
                        '\nProps:', self.props_to_html()])

    def to_html(self):
        raise NotImplementedError("Not Implemented")

    def props_to_html(self):
        '''
        Returns a string that represents the HTML attributes of the node
        '''
        if self.props == None:
            return str(None)
        return ''.join([f' {key}="{value}"' for (key,value) in self.props.items()])


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, props=props)

    def to_html(self):
        if self.value == None:
            raise ValueError("All LeafNodes must have a value")
        if self.tag == None:
            return str(self.value)
        if self.props == None:
            return f'<{self.tag}>{self.value}</{self.tag}>'
        return f'<{self.tag}{super().props_to_html()}>{self.value}</{self.tag}>'

        


