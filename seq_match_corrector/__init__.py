from difflib import SequenceMatcher

def ratios(target: list, dictionary: list) -> list:
    def ratio(word: str):
        if not word: return
        l = len(word)
        return sorted(
            filter(
                lambda x: x[1] > 0.5,
                map(lambda x: [x, SequenceMatcher(None, x, word).ratio()], filter(lambda x: len(x) in range(l - 2, l + 3), dictionary))
            ), key=lambda x: x[1], reverse=True
        )
    return list(
        filter(lambda x: x, map(ratio, target))
    )

def correct(target: list, dictionary: list) -> dict:
    r = ratios(target, dictionary)
    result = {}
    for i in range(len(target)):
        if r[i]:
            result[target[i]] = r[i][0][0]
        else:
            result[target[i]] = target[i]
    return result