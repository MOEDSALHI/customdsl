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

def get_data_field(file):
    """this function retun data from JSON

    Args:
        file (string): path to json file

    Returns:
        JSON object: data
    """
    with open(file) as data_file:
        return json.load(data_file)["fields"]


def get_data_filter(file):
    """this function retun data from JSON

    Args:
        file (string): path to json file

    Returns:
        JSON object: data
    """
    with open(file) as data_file:
        return json.load(data_file)["filters"]

def check_existing_field(field_name):
    """this function is used to check existing field into SQL_TABLE_SCHEMA

    Args:
        field_name (string): the field name to check

    Returns:
        boolean: return true if field_name exist in SQL_TABLE_SCHEMA
        else return false
    """
    for elt in SQL_TABLE_SCHEMA:
        if elt["name"] == field_name:
            return True
    return False


def get_type_field(field_name):
    """this function is used to get type field

    Args:
        field_name (string): the field name to get here type

    Returns:
        string: the type of field_name
    """
    for elt in SQL_TABLE_SCHEMA:
        if elt["name"] == field_name:
            return elt["type"]