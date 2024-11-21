import pytest
from pytestDemo.BaseClass import BaseClass

# CMD: py.test --html=report.html -s

@pytest.mark.usefixtures("dataLoad")
class TestExample2(BaseClass):

    def test_editProfile(self, dataLoad):
        log = self.getLogger()
        log.info(dataLoad[0]) # For log info
        log.info(dataLoad[2])
        print(dataLoad[2])