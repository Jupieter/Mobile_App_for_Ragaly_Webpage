# from soap import HtmlTransformer
import soap

def test_link_find(): 
    # data_in = '<p><strong>Hello World</strong></p>'
    data_in = '''
        <p><strong>Hello World</strong></p> 
        <p><a href="http://ragaly.hu/wp-content/uploads/2020/09/Plakat_2021-2.jpg">
        <img class="size-large wp-image-42622 aligncenter" 
        src="http://ragaly.hu/wp-content/uploads/2020/09/Plakat_2021-2-714x1024.jpg" 
        alt="" width="676" height="970" /></a></p>'''
    data_out = ["http://ragaly.hu/wp-content/uploads/2020/09/Plakat_2021-2.jpg"] 
    # data_out = ""
    # tr = HtmlTransformer()
    # print(tr)
    print(data_in)
    test1 = soap.link_find(data_in)
    print(test1)
    assert test1 == data_out