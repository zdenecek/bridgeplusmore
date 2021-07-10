def truncate(text: str, chars = 75, elipsis = '..') -> str:
    return text if len(text) <= chars else text[0:chars] + elipsis