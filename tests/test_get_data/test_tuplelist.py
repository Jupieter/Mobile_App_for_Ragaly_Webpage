from get_data import DB_questions


def test_transformlist():
    data_in =  [(1234, "ZOZO", 5678, "NONONONO","2022.10.07"), (12121,"XOXO", 666999, "Dosn't matter", "2022.10.08")]
    data_out = [[1234, "ZOZO", 5678, "NONONONO","2022.10.07"], [12121,"XOXO", 666999, "Dosn't matter", "2022.10.08"]]
    tr = DB_questions()
    test1 = tr.list_from_tuple(data_in)
    print(test1)
    assert test1 == data_out