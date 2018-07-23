from bs4 import BeautifulSoup
from sys import argv
import spacy
import textacy
import requests
import re

RE_STRIP_REFS = re.compile("\.?\[\d+\]?")
NLP = spacy.load('en_core_web_sm')
REPLACE_VERBS = {
    "being" : "was",
    "to be" : "will be"
}

def cleanup(s):
    s = RE_STRIP_REFS.sub("", s).strip()

    # Pretty ugly
    if s[-1] == ".":
        s = s[0:-1]

    return s

def cleanup_verb(verb):
    if verb in REPLACE_VERBS:
        verb = REPLACE_VERBS[verb]

    return verb

def get_article_text(title):
    ENDPOINT = f"https://en.wikipedia.org/api/rest_v1/page/html/{title}"
    req = requests.get(ENDPOINT)
    soup = BeautifulSoup(req.text, "lxml")
    text = soup.select("body")[0].get_text().strip()
    return text

def get_statements_from_text(text, article):
    doc = NLP(text)
    statements = textacy.extract.semistructured_statements(doc, article)
    return list(statements)

def main():
    article = " ".join(argv[1:])
    print(f"Did you know that {article}...")

    text = get_article_text(article)
    statements = get_statements_from_text(text, article)

    if len(statements) == 0:
        print(f"forget that, i know nothing of interest on {article}")

    for statement in statements:
        subject, verb, fact = statement
        fact = cleanup(str(fact))
        verb = cleanup_verb(str(verb))
        print(f"...{verb} {fact}?")

if __name__ == "__main__":
    main()