import re


def preprocess(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9]", " ", text)
    return text.split()


result = preprocess("117\nRAIGARH-CG\nChattisgarh")
print(result)
