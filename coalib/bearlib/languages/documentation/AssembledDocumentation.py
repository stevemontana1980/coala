from coalib.bearlib.languages.documentation.DocumentationComment import (
    DocumentationComment)

Description = DocumentationComment.Description
Parameter = DocumentationComment.Parameter
ReturnValue = DocumentationComment.ReturnValue


def assemble_documentation(doccomment, param_sym, ret_sym):
    """
    Assembles a list of parsed documentation comments.

    This function just assembles the documentation comment
    itself, without the markers and indentation.

    :param doccomment:
        The list of parsed documentation comments.
    :param param_sym:
        A two element tuple that defines how a param definition starts and
        ends in a documentation comment.
    :param ret_sym:
        A string that defines how a return statement definition occurs in
        a documentation comment.
    """
    assembled_doc = ""
    for section in doccomment:
        section_desc = section.desc.splitlines(keepends=True)
        if isinstance(section, Description):
            assembled_doc += section_desc[0]
        elif isinstance(section, Parameter):
            assembled_doc += (param_sym[0] + section.name + param_sym[1] +
                              section_desc[0])
        elif isinstance(section, ReturnValue):
            assembled_doc += ret_sym + section_desc[0]
        for desc in section_desc[1:]:
            if desc != "":
                assembled_doc += desc
    return assembled_doc


def assemble_full_documentation(doccomment, param_sym, ret_sym,
                                markers, indent):
    """
    Assembles a list of parsed documentation comments.

    This function assembles the whole documentation comment,
    with the given markers and indentation.

    :param doccomment:
        The list of parsed documentation comments.
    :param param_sym:
        A two element tuple that defines how a param definition starts and
        ends in a documentation comment.
    :param ret_sym:
        A string that defines how a return statement definition occurs in
        a documentation comment.
    :param markers:
        The markers to be used.
    :param indent:
        The indentation level to be used for each line of the documentation
        comment.
    """
    assembled_doc = assemble_documentation(doccomment, param_sym, ret_sym)
    assembled_doc = assembled_doc.splitlines(keepends=True)
    assembled = indent + markers[0]
    for section in assembled_doc:
        if section == "\n":
            assembled += '\n'
        else:
            assembled += indent + markers[1] + section
    return assembled + indent + markers[2]
