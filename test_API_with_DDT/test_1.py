from main import check_works

def test_step1(good, bad):
    assert good in check_works(bad)
