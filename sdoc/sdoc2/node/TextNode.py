"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
import re
import sdoc
from sdoc.sdoc2 import node_store
from sdoc.sdoc2.node.Node import Node
from sdoc.sdoc2.node.EndParagraphNode import EndParagraphNode


class TextNode(Node):
    """
    SDoc2 node for items.
    """
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        super().__init__('TEXT')

    # ------------------------------------------------------------------------------------------------------------------
    def print_info(self, level):
        """
        Temp function for development.

        :param int level: the level of block commands.
        """
        print("%s%4d %s %s" % (' ' * 4*level, self.id, self.name, ''))

    # ------------------------------------------------------------------------------------------------------------------
    def is_block_command(self):
        """
        Returns False.

        :rtype: bool
        """
        return False

    # ------------------------------------------------------------------------------------------------------------------
    def is_inline_command(self):
        """
        Returns False.

        :rtype: bool
        """
        return False

    # ------------------------------------------------------------------------------------------------------------------
    def is_phrasing(self):
        """
        Returns True.

        :rtype: bool
        """
        return True

    # ------------------------------------------------------------------------------------------------------------------
    def splitted_text(self):
        """
        Method which takes text and splits it by newlines, creates text nodes,
        sets id's to text nodes, put id's in list and returns list of id's.

        :param sdoc.sdoc2.node.TextNode.TextNode text: Whole text

        :rtype: list[int]
        """
        text_ids = []
        list_of_texts = re.split("\n\n", self.argument)

        # Cleaning the text parts.
        if "\n" in list_of_texts:
            list_of_texts[list_of_texts.index("\n")] = ''
        if list_of_texts[0] == '':
            list_of_texts.remove('')

        # Checking the range.
        if list_of_texts:
            if not list_of_texts[-1]:
                to = len(list_of_texts) - 1
            else:
                to = len(list_of_texts)

            # Creating text and paragraph end nodes and put id's in list.
            for text in list_of_texts[:to]:
                text_node = TextNode()
                sdoc.sdoc2.node_store.store_node(text_node)
                text_node.argument = text
                text_ids.append(text_node.id)

                end_paragraph_node = EndParagraphNode()
                sdoc.sdoc2.node_store.store_node(end_paragraph_node)
                text_ids.append(end_paragraph_node.id)

            # Checking where we need to add paragraph.
            if len(text_ids):
                if list_of_texts[-1]:
                   text_ids.pop()

        return text_ids

# ----------------------------------------------------------------------------------------------------------------------
node_store.register_inline_command('TEXT', TextNode)