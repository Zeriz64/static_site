class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        attribute = ""
        if self.props == None:
            return attribute
        for key, value in self.props.items():
            attribute = attribute + f' {key}="{value}"'
        return attribute
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, Children: {self.children}, {self.props})"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Missing tag on Parent Node.")
        if self.children == None:
            raise ValueError("Missing Children on Parent Node.")
        list_of_children = ""        
        for child in self.children:
            list_of_children += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{list_of_children}</{self.tag}>"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("Missing value on Leaf Node.")
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"