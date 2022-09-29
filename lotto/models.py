from django.db import models

from django.db import models
from django.utils import timezone
import random

# Create your models here.
class GuessNumbers(models.Model):
    # 중요! 필드를 구성하거나, 변경했을 때 DB에 반영해 줘야 함 -> db.sqlie3 파일에 생성됨
    name = models.CharField(max_length=24) # 로또 번호 리스트의 이름
    text = models.CharField(max_length=255) # 로또 번호 리스트에 대한 설명
    lottos = models.CharField(max_length=255, default='[1, 2, 3, 4, 5, 6]') # 로또 번호들이 담길 str
    num_lotto = models.IntegerField(default=5) # 6개 번호 set의 갯수
    update_date = models.DateTimeField()

# generate 함수를 models.py에 만들어 놓는것은 선택사항 이며,
# 저장하거나, 계산하는 종류의 함수들은 views.py파일에 만들어 놓는다.
# 여기 예제에서는 models.py에도 만들 수 있다는 것을 보여주기 위한 예시이다.
    def generate(self): # 로또 번호를 자동으로 생성
        self.lottos = "" # 디폴트로 받아온 값들을 빈 문자열로 만들어줌
        origin = list(range(1,46)) # 1~45의 숫자 리스트 [1, 2, 3, ..., 43, 44, 45]

        # 6개 번호 set 갯수만큼 1~46 뒤섞은 후 앞의 6개 골라내어 sorting
        for _ in range(0, self.num_lotto): # num_lotto에 들어있는 숫자가 5라면 -> range(0, 5)
            random.shuffle(origin) # 랜덤을 섞음 -> [10, 21, 36, 2, ... , 1, 11]
            guess = origin[:6] # 앞에서 6자리까지 split -> [10, 21, 36, 2, 15, 23]
            guess.sort() # 정렬 -> [2, 10, 15, 21, 23, 36]
            self.lottos += str(guess) +'\n' # 로또 번호 변수에 6개 번호 set을 str로 변환한뒤 '\n'(카운트 슬레시)를 더 한후 추가 
            # -> '[2, 10, 15, 21, 23, 36]\n'
            # self.lottos : '[2, 10, 15, 21, 23, 36]\n[1, 15, 21, 27, 30, 41]\n...'
        self.update_date = timezone.now() # 현재 날짜 시간을 불러와 저장함(settings.py에서 설정한 영향을 받음)
        self.save() # GuessNumbers object를 DB에 저장

    def __str__(self): # Admin page에서 display되는 텍스트에 대한 변경
        return "pk {} : {} - {}".format(self.pk, self.name, self.text) # pk는 프라이머리키를 말하며, 자동생성됨


