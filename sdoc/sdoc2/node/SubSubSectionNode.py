"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.sdoc2 import node_store
from sdoc.sdoc2.node.HeadingNode import HeadingNode


class SubSubSectionNode(HeadingNode):
    """
    SDoc2 node for sub subsections.
    """
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, options, argument):
        """
        Object constructor.

        :param dict[str,str] options: The options of this section.
        :param str argument: The title of this section.
        """
        super().__init__('sub_subsection', options, argument)

    # ------------------------------------------------------------------------------------------------------------------
    def get_hierarchy_level(self):
        """
        Returns 4.

        :rtype: int
        """
        return 4

# ----------------------------------------------------------------------------------------------------------------------
node_store.register_inline_command('sub_subsection', SubSubSectionNode)

