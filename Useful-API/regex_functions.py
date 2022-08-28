import re
# Capitalizes the first letter of uncamelcased word
def camelCaseToLabel(str: str) -> str:
    label = re.sub(r'((?<=[a-z])[A-Z]|(?<!\A)[A-Z](?=[a-z]))', r' \1', str)
    label = label[0].upper() + label[1:]
    return label

