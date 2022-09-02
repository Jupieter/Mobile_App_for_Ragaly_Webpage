import pytest
from get_data import DB_questions


def test_ids_revision():
    myresult_in = [
        [17, "Post 1", 15, "<p><strong>Hello World</strong></p>"], 
        [16, "Post 1", 15, "<p><strong>Hello World</strong></p>"],
        [15, "Post 1", 0, "<p><strong>Hello World</strong></p>"],
        [14, "Post 2", 10, "<!-- wp:tadv/classic-paragraph -->\n<p><strong>A versenyekről röviden</strong></p>\n<p>Nevezés:"]
        ]
    result_out = [
        [17, "Post 1", 15, "<p><strong>Hello World</strong></p>"], 
        [14, "Post 2", 10, "<!-- wp:tadv/classic-paragraph -->\n<p><strong>A versenyekről röviden</strong></p>\n<p>Nevezés:"]
        ]
    tr = DB_questions()
    test1 = tr.post_ids(myresult_in)
    assert test1 == result_out

def test_ids_empty_html():
    myresult_in = [
        [17, "Post 1", 15, "<p><strong>Hello World</strong></p>"], 
        [16, "Post 1", 15, "<p><strong>Hello World</strong></p>"],
        [15, "Post 1", 0, "<p><strong>Hello World</strong></p>"],
        [14, "Post 3", 0, ""],
        [13, "Post 2", 10, "<!-- wp:tadv/classic-paragraph -->\n<p><strong>A versenyekről röviden</strong></p>\n<p>Nevezés:"]
        ]
    result_out = [
        [17, "Post 1", 15, "<p><strong>Hello World</strong></p>"], 
        [13, "Post 2", 10, "<!-- wp:tadv/classic-paragraph -->\n<p><strong>A versenyekről röviden</strong></p>\n<p>Nevezés:"]
        ]
    tr = DB_questions()
    test1 = tr.post_ids(myresult_in)
    assert test1 == result_out

def test_ids_early_rev():
    myresult_in = [
        [20, "Post 1", 15, "<p><strong>Hello World</strong></p>"], 
        [19, "Post 1", 15, "<p><strong>Hello World</strong>"],
        [18, "Post 3", 0, ""],
        [17, "Post 2", 10, "<!-- wp:tadv/classic-paragraph -->\n<p><strong>A versenyekről röviden</strong></p>\n<p>Nevezés:"],
        [15, "Post 1", 0, "<p><strong>Hello World"],
        [14, "Post 2", 0, "<!-- wp:tadv/classic-paragraph -->\n<p><strong>A versenyekről röviden</strong></p>\n<p>Nevezés:"]
        ]
    result_out = [
        [20, "Post 1", 15, "<p><strong>Hello World</strong></p>"], 
        [17, "Post 2", 10, "<!-- wp:tadv/classic-paragraph -->\n<p><strong>A versenyekről röviden</strong></p>\n<p>Nevezés:"]
        ]
    tr = DB_questions()
    test1 = tr.post_ids(myresult_in)
    assert test1 == result_out