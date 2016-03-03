"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
import antlr4

import sdoc
from sdoc.antlr.sdoc2Lexer import sdoc2Lexer
from sdoc.antlr.sdoc2Parser import sdoc2Parser
from sdoc.sdoc2.SDoc2visitor import SDoc2Visitor


class SDoc2Interpreter:
    """
    Class for processing SDoc1 documents.
    """
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        """
        Object constructor.
        """
        pass

    # ------------------------------------------------------------------------------------------------------------------
    def process(self, infile):
        """
        Processes a SDoc1 document.

        :param str infile: The input filename with the SDoc2 document.
        """
        in_stream = antlr4.FileStream(infile, 'utf-8')

        lexer = sdoc2Lexer(in_stream)
        tokens = antlr4.CommonTokenStream(lexer)
        parser = sdoc2Parser(tokens)
        tree = parser.sdoc()
        visitor = SDoc2Visitor()

        visitor.visit(tree)

        sdoc.sdoc2.node_store.prepare_content_tree()
        sdoc.sdoc2.node_store.number_numerable()


# ----------------------------------------------------------------------------------------------------------------------
