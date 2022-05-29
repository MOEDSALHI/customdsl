from common import get_type_field, check_existing_field, COMPARISON_OPERATORS


def filtering(data):
    """this is a function to implement simple filtering

    Args:
        data (dict): JSON Object (in a cusrtom DSL)

    Returns:
        string : a string corresponding to the WHERE clause query
    """

    where_clause = ""
    if isinstance(data, dict):
        if "predicate" not in data:
            if get_type_field(data["field"]) == "str":
                where_clause += "{} = '{}'".format(
                    data["field"], data["value"])
            else:
                where_clause += "{} = {}".format(data["field"], data["value"])
        else:
            if check_existing_field(data["field"]):
                if get_type_field(data["field"]) == "str":
                    where_clause += "{} {} '%{}%'".format(
                        data["field"], COMPARISON_OPERATORS[data["predicate"].upper()], data["value"])
                else:
                    where_clause += "{} {} {}".format(
                        data["field"], COMPARISON_OPERATORS[data["predicate"].upper()], data["value"])
            else:
                print("Field {} does not valid ".format(data["field"]))
    return where_clause
