
def generate_field_selection(data):
    """this is a function to only support quering field selectors

    Args:
        data (dict): JSON Object (in a cusrtom DSL)

    Returns:
        string : a string corresponding to the SELECT clause query
    """

    select_clause = ""
    if isinstance(data, list):
        select_clause = ", ".join(data)
    return select_clause
