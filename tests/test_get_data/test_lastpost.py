from get_data import DB_questions


def test_lastpost():
    data_in = ((42624, 42592), (42623, 42592), (42622, 42592), (42620, 42592), (42617, 42592), (42595, 42592), (42593, 42592), (41243, 41241), (41242, 41241), (880, 515), (516, 515))
    data_out = [42624, 41243, 880]
    tr = DB_questions()
    test1 = tr.post_last(data_in)
    print(test1)
    assert test1 == data_out