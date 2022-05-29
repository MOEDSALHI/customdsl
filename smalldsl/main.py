from common import get_data

def main():
    fields = get_data(".\examples\json_dsl_field_selection.json")["fields"]
    return fields


if __name__ == '__main__':
    print(main())