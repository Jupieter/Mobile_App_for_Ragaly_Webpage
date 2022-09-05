import pytest
# from soap import HtmlTransformer
import transform


def test_transform():
    post_in = [
        [15, "Post 1", 12, "<p><strong>Hello World</strong></p>", "2017-07-10 16:32:05"], 
        [14, "Post 2", 10, "<!-- wp:tadv/classic-paragraph -->\n<p><strong>A versenyekről röviden</strong></p>\n<p>Nevezés:", "2022-02-22 22:22:22"],
        [13, "Post 3", 8, 
        '''<p><strong>JuPYther</strong></p> 
        <p><a href="http://ragaly.hu/wp-content/uploads/2020/09/Plakat_2021-2.jpg">
        <img class="size-large wp-image-42622 aligncenter" 
        src="http://ragaly.hu/wp-content/uploads/2020/09/Plakat_2021-2-714x1024.jpg" 
        alt="" width="676" height="970" /></a></p>''',
         "2022-02-22 22:22:22"]
        ]
    post_out = [
        [15, 'Post 1', 12, '[b]Hello World[/b]', '2017-07-10 16:32:05', []], 
        [14, 'Post 2', 10, '\n[b]A versenyekről röviden[/b]\nNevezés:', '2022-02-22 22:22:22', []],
        [13, 'Post 3', 8, '[b]JuPYther[/b]\n\n', '2022-02-22 22:22:22', ['http://ragaly.hu/wp-content/uploads/2020/09/Plakat_2021-2.jpg']]
        ]
    test2 = transform.transform(post_in)
    for i in test2:
        print("test2_[i]:   ", i)
    assert test2 == post_out
