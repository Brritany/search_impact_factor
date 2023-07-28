import pandas as pd
import pkg_resources

_df = None  # Global variable for the database

def load_database(year="2023"):
    global _df
    version = f"{year}_JCR_IF.csv"
    file_path = pkg_resources.resource_filename('search_impact_factor', version)
    _df = pd.read_csv(file_path)


def query_database(query_dict):
    """
    Query the DataFrame based on the conditions specified in the query_dict.

    Parameters:
    - query_dict: A dictionary where the keys are column names and the values are the values to match.

    Returns:
    - A list of dictionaries, where each dictionary represents a row in the DataFrame that matches the query.
    """
    # Start with the entire DataFrame
    result_df = _df.copy()

    # Filter the DataFrame based on the conditions in query_dict
    for column, value in query_dict.items():
        if column == 'Journal':
            # Ignore case and allow partial match for 'Journal' column
            result_df = result_df[result_df[column].str.contains(value, case=False, na=False)]
        elif column == 'Category':
            # Ignore case for 'Category' column
            result_df = result_df[result_df[column].str.contains(value, case=False, na=False)]
        else:
            # For other columns, perform exact match
            result_df = result_df[result_df[column] == value]

    # If the resulting DataFrame is empty, return an error message
    if result_df.empty:
        return "Please check your input is correct OR This journal is not indexed in SCIE or SSCI"

    # Convert the resulting DataFrame to a list of dictionaries and return it
    return result_df.to_dict('records')


def query_if_score(min_score, max_score):
    result_df = _df[_df['IF'].between(min_score, max_score)]
    return result_df

