import json

LOGICAL_OPERATORS = ("AND", "OR")

COMPARISON_OPERATORS = {
    "LT": "<",
    "GT": ">",
    "LTE": "<=",
    "GTE": ">=",
    "EQ": "=",
    "NEQ": "!=",
    "CONTAINS": "like"
}

SQL_TABLE_SCHEMA = [
    {"name": "code", "type": "int"},
    {"name": "name", "type": "str"},
    {"name": "population", "type": "int"},
    {"name": "average_age", "type": "float"},
    {"name": "distr_code", "type": "int"},
    {"name": "dept_code", "type": "int"},
    {"name": "region_code", "type": "int"},
    {"name": "region_name", "type": "str"}
]


def get_data(file):
    """this function retun data from JSON

    Args:
        file (string): path to json file

    Returns:
        JSON object: data
    """
    with open(file) as data_file:
        return json.load(data_file)
