from django.test import TestCase
from .models import GuessNumbers

# Create your tests here.
# 잘 저장되어있는지 테스트 할 수 있는 테스트 케이스 만들기
class GuessNumbersTestCase(TestCase):

    def test_generate(self):
        g = GuessNumbers(nmae='Test numbers', text='selected number')
        g.generate()

        print(g.update_date) # 업데이트 된 날짜 확인
        print(g.lottos) # 로또 번호 확인

        self.assertTrue(len(g.lottos) > 20) # lottos의 조건이 참인지 검사