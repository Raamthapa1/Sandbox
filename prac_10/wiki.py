"""Testing wikioedia serach from input """

import wikipedia


def search_wiki():
    """Takes inpput and return title, summary and URL form wikipedia"""
    search = input("What do you want to search?: ")
    wiki_search = wikipedia.page(search, auto_suggest=False)
    print(f'Title \n{wiki_search.title} \n \nSummary \n{wiki_search.summary} \n \nURL \n{wiki_search.url}')


search_wiki()
