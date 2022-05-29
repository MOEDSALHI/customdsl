from filtering import filtering


def filter_compounding(data):
    """this is a function to implement a feature allowing to chain
    multiple filters through a boolean operator

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
            if len(val[1]) == 1:
                where_clause += "{} {} ({})".format(filter_compounding(val[0]),
                                                    key,
                                                    filter_compounding(val[1]))
            else:
                where_clause += "{} {} {}".format(filter_compounding(val[0]),
                                                  key,
                                                  filter_compounding(val[1]))
    return where_clause
