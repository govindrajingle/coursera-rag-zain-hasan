import re


def preprocess(text):
    """
    Convert text into clean searchable tokens
    """

    text = text.lower()

    text = text.replace("_", " ")

    text = re.sub(r"[^a-z0-9 ]", " ", text)

    tokens = text.split()

    return tokens


if __name__ == "__main__":

    print(preprocess("EAST_GODAVARI"))

    print(preprocess("KHAMMAM/BHADRACHALAM"))

    print(preprocess("Andhra Pradesh"))
