# Define a function that formats city and country information,
# with optional population and language parameters.
def city_country(city, country, population=None, language=None):

    if language is not None and population is not None:
        return f"{city}, {country} - population {population}, {language}"

    elif population is not None:
        return f"{city}, {country} - population {population}"

    elif language is not None:
        return f"{city}, {country} - language {language}"

    else:
        return f"{city}, {country}"
