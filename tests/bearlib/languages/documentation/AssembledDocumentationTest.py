import unittest

from coalib.bearlib.languages.documentation.AssembledDocumentation import (
    assemble_documentation, assemble_full_documentation)
from coalib.bearlib.languages.documentation.DocumentationExtraction import (
    extract_documentation)
from tests.bearlib.languages.documentation.TestUtils import (
    load_testdata)


class AssembledDocumentationTest(unittest.TestCase):

    def test_python_assembly(self):

        data = load_testdata("default.py")

        original = [doc.documentation for doc in
                    extract_documentation(data, "python", "default")]

        parsed_docs = [(doc.parse(), doc.marker, doc.indent) for doc in
                       extract_documentation(data, "python", "default")]

        param = ":param ", ":"
        ret = ":return:"

        self.assertEqual([assemble_documentation(doc[0], param, ret)
                          for doc in parsed_docs], original)

        for assembled_doc in (assemble_full_documentation(doc[0], param, ret,
                                                          doc[1], doc[2])
                              for doc in parsed_docs):
            self.assertIn(assembled_doc, "".join(data))
