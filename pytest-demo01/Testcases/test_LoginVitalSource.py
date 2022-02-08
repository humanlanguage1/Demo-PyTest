from Pages.Page_LoginVitalSource import LoginVitalSource


class test_SignUpTest:

    def test_Login_Successful(BaseTest):
        regPage = LoginVitalSource(self.driver)
        regPage.doLogin("edwin.coronado@vitalsource.com", "zR04iowfabcABC##")
