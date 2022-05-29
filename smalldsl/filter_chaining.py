from filtering import filtering


def filter_chaining(data):
    """this is a function to extend filter chaining to allow compounding
    filters using AND or OR condition

    Args:
        data (dict): JSON Object (in a cusrtom DSL)

    Returns:
        string : a string corresponding to the WHERE clause query
    """

    where_clause = ""
    if isinstance(data, dict):
        if len(data) != 1:
            where_clause += filtering(data)
        else:
            [(key, val)] = data.items()
            where_clause += "{} {} {}".format(filter_chaining(val[0]),
                                              key,
                                              filter_chaining(val[1]))
    return where_clause
