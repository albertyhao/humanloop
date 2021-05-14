from snorkel.labeling import LabelingFunction

def make_keyword_lf(keywords, label=1):
    def keyword_lookup(x, keywords, label):
        if any(word in x.text.lower() for word in keywords):
            return label
        return -1

    return LabelingFunction(
        name=f"keyword_{keywords[0]}",
        f=keyword_lookup,
        resources=dict(keywords=keywords, label=label),
    )
