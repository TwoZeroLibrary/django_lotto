from django.shortcuts import render, redirect
from django.http import HttpResponse
from lotto.models import GuessNumbers
from .forms import PostForm


# 참고 : 파이썬에서는 함수와 함수 사이에 줄바꿈을 2번 해준다
def hello(request):
    # data = GuessNumbers.objects.all() # sql에서 selct all과 같은 기능, 모든 열 가져오기

    return HttpResponse("<h1 style='color:red;'>Hollo, world!</h1>") # 예시 테스트 코드


def index(request):
    # return HttpResponse('<h1>Hollo, wrold!</h1>') # 예시 테스트 코드

    lottos = GuessNumbers.objects.all() # DB에 저장된 GuessNumbers 객체 모두를 가져온다.
    # 브라우저로부터 넘어온 request를 그대로 template('default.html')에게 전달
    # {} 에는 추가로 함께 전달하려는 object들을 dict로 넣어줄 수 있으며, context-dict라고도 부름
    return render(request, 'lotto/default.html', {'lottos':lottos}) # request(유저의 요청), 유저에게 돌려줄 html을 포함한 경로이름(보통 urls.py의 path에 있는 이름들로 통일함),  


def post(request):

    # print('\n\n\n')
    # print(request.method) # 요청하거나 응답 받을 때 CMD창을 확인해보면 GET과 POST라고 출력되는 것을 볼 수 있음
    # print(request.POST) # 응답받을 때 CMD 창을 보면 아래와 같은 결과를 받을 수 있음
    # # <QueryDict: {'csrfmiddlewaretoken': ['JD7y0yhpbtgvSSxjtQrKnCGsXM8ZWDXhpcRSArdRO1H8Tt2nO0NSzYsi8xin1B9o'], 
    # # 'name': ['응답이 잘가는지'], 'text': ['테스트 중']}>
    # print('\n\n\n')

    if request.method == "POST":
        # print(request.POST) # 주석을 풀면 새로운 로또 번호 생성 후 cmd에서 이 값을 확인할 수 있음
        # print(request.method) # 주석을 풀면 새로운 로또 번호 생성 후 cmd에서 이 값을 확인할 수 있음
        # 사용자로부터 넘겨져 온 POST 요청 데이터를 담아 PostForm 객체 생성
        form = PostForm(request.POST) # 채워진 양식
        # 만약 여기서 후처리를 할 필요가 없다면 바로 form.save() 함수를 사용하여 저장하면 된다.
        # 하지만 현실습에서는 후처리가 필요하므로 바로 저장하지 않는다.

        # print(type(form)) # <class 'lotto.forms.PostForm'>
        # print(form)
        if form.is_valid(): # 유저가 입력한 값이 형식에 맞는지 확인
        # commit = False -> 사용자로부터 입력받은 form 데이터에서 추가로 수정해주려는 사항이 있을 경우 save를 보류함
            lotto = form.save(commit = False) # 최종 DB 저장은 아래 generate 함수 내부의 .save()로 처리 함
            # print(type(lotto)) # 출력결과 -> <class 'lotto.models.GuessNumbers'> # GuessNumbers 객체변수 클래스(== 테이블의 하나의 행) 자체가 저장되어 있음
            # print(lotto) # 출력결과 -> pk None : 테스트 입니다 - 안녕하세요 # 저장이 되지 않았기 때문에 id 값이 None으로 나옴
            lotto.generate() # 테이블에 저장
            return redirect('index') # urls.py의 name='index'에 해당
            # -> 상단 from django.shortcuts import render, redirect 수정
    else:
        form = PostForm() # 빈 양식 만듦
        return render(request, "lotto/form.html", {"form": form})


def detail(request, lottokey):
    lotto = GuessNumbers.objects.get(pk = lottokey) # primary key, id로도 사용가능함
    return render(request, "lotto/detail.html", {"lotto": lotto}) # htmal 넘겨주기

    