from django import forms
from .models import GuessNumbers

# Django에서 제공하는 ModelForm을 활용해 form 구성
# 즉, forms.ModelForm는 models.py에 있는 GuessNumbers 클래스에서 구성한 필드를 활용함
class PostForm(forms.ModelForm):

    # Form을 통해 받아들여야할 데이터가 명시되어 있는 메타 데이터 (DB 테이블을 연결)
    class Meta:
        model = GuessNumbers
        fields = ('name', 'text',) # 사용자로부터 form 통해 입력받을 데이터, name과 text만 받겠다는 의미이며, 텍스트로 입력하면 됨
