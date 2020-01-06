from django.shortcuts import render
from django.http import JsonResponse
from .utils import makechartdef

# 크롤링중
# 예매율 1~100퍼센트이상만 보도록 기능설정가능
# 크롤링 먼저 구현해보기
# 다음 영화
# 등등 각자 사잍의 네이즌 평점 크롤링 구현
# 비교 그래프를 표현하고
# 누르면 해당 영화를 검색해주는 것까지(그림, 텍스트 둘다)

def comeon(request):
    data = makechartdef()

    return render(request, 'mychart2/index.html', {'soup':'고양이'})



def makechart(request):
    data = makechartdef()

    return JsonResponse({
        'labels': [ ep['title'] for ep in data['data_list']],
        'datasets': [{
            'label': '평점',
            'backgroundColor': "rgba(255, 99, 132, 0.5)",
            'borderColor': "rgba(255, 99, 132, 1)",
            'pointBackgroundColor': "rgba(255, 99, 132, 1)",
            'pointBorderColor': "#fff",
            'data': [ep['rating'] for ep in data['data_list']]
        }],

    })