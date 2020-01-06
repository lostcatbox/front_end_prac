import time
from django import template
from django.conf import settings
from django.templatetags.static import StaticNode

register = template.Library()

class VersioningStaticNode(StaticNode):  #장고에서 기본 지원해주는 템플릿 태그
     def url(self, context):
         url = super().url(context)  #기존 스테틱노드에서 url얻고
         if settings.DEBUG:  #개발모드 일때만
             t = str(int(time.time())) #소수점까지 붙는 시간을 int로 정수형반환>문자열로 반환
             if '?' not in url:     #(url안에 ? 없다면)
             		url += '?_=' + t
             else:
             		url += '&_=' + t   #?가 이미있다면 get인자가 이미존재하는것이므로 &_뒤에씀
         return url

@register.tag('static_t')
def static_t(parser, token):
		 return VersioningStaticNode.handle_token(parser, token)