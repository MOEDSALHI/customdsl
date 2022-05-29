from common import get_data
from field_selection import generate_field_selection


def main():
    fields = get_data(".\examples\json_dsl_field_selection.json")["fields"]
    select_clause = generate_field_selection(fields)
    return "SELECT {} \nFROM Town".format(select_clause)


if __name__ == '__main__':
    print(main())