import pytest
# from soap import HtmlTransformer
import soap

def test_markup_strong():
    html_in = "<p><strong>Hello World</strong></p>"
    kivy_out = "<p>[b]Hello World[/b]</p>"
    # tr = HtmlTransformer()
    test1 = soap.strong_murkup(html_in)
    assert test1 == kivy_out