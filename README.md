# Extract 'Did you know?' facts from Wikipedia articles

This is a small Python command line tool and a Jupyter Notebook based on Adam Geitgey's [excellent blogpost](https://medium.com/@ageitgey/natural-language-processing-is-fun-9a0bff37854e) on Natural Language Processing in Python.

When you run the command like this

    $ python3 wiki-text-nlp.py Pikachu

It will show you 'interesting facts' based on the article on the English Wikipedia.

    Did you know that Pikachu...
    ...is a central character in the Pokémon anime series?
    ...was one of several different Pokémon designs conceived by Game Freak's character development team?
    ...were the first "Electric-type" Pokémon created, their design intended to revolve around the concept of electricity?
    ...is one of the sixteen starters and ten partners in the Pokémon Mystery Dungeon games?
    ...is an amiibo character?
    ...would be happier living in a colony of wild Pikachu?
    ...is one of the main Pokémon used in many of the Pokémon manga series?
    ...is real, out next week in Japan?

# Dependencies
If you've followed [Adam's tutorial](https://medium.com/@ageitgey/natural-language-processing-is-fun-9a0bff37854e) you'll have all the dependencies expect for two: `bs4` (BeautifulSoup) and `requests`.

If you haven't followed that tutorial, this will help you out

    pip3 install spacy textacy bs4 requests

You also need to install the 'small' English model for spaCy:

    python3 -m spacy download en_core_web_sm

I probably should be making a requirements.txt or a Pipfile, but i'm lazy.

# Credits
This code was based on [this little gist](https://gist.github.com/ageitgey/99debc6682295d1580fff1b803648dd4) by Adam Geitgey. The rest was done by [Hay Kranen](https://www.haykranen.nl/).

The Wikipedia content is retrieved from the excellent [Wikimedia REST API](https://en.wikipedia.org/api/rest_v1/) which more people should use.

Given that this is mostly a textbook example, this code is in the public domain.