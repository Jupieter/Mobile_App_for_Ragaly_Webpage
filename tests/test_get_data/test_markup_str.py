import pytest
from get_data import DB_questions


def test_markup_strong():
    html_in = "<p><strong>Hello World</strong></p>"
    kivy_out = "<p>[b]Hello World[/b]</p>"
    tr = DB_questions()
    test1 = tr.strong_murkup(html_in)
    print(test1)
    # assert test1 == kivy_out