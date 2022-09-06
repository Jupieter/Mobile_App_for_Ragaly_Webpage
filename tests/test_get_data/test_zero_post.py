from tests.get_data import DB_questions


def test_zero():
    data_in = [[24, "Post 1", 0, "abcdef"]]
    data_out = [[24, "Post 1", 24, "abcdef"]]
    tr = DB_questions()
    test1 = tr.zero_post_type(data_in)
    print(test1)
    assert test1 == data_out