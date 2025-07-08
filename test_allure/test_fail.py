import allure

def test_fail():
    allure.attach(b"abc123", name="demo", attachment_type=allure.attachment_type.PNG)
    assert False
