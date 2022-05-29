from common import get_data_field, get_data_filter
from field_selection import generate_field_selection
from filtering import filtering
from filter_chaining import filter_chaining
from filter_compounding import filter_compounding


def main():
    path_file = ".\examples\json_dsl_filter_compounding.json"
    
    # get field from data
    fields = get_data_field(path_file)
    # generate select clause
    select_clause = generate_field_selection(fields)

    # get filter from data
    filters = get_data_filter(path_file)
    # generate where clause 
    where_clause = filter_compounding(filters)

    return "SELECT {} \nFROM Town \nWHERE {}".format(select_clause,
                                                      where_clause)


if __name__ == '__main__':
    print(main())