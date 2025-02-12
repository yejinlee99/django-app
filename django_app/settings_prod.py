# EB (EC2) 운영환경
from .settings import *

# 운영 환경 반드시 False로 설정 할 것!!
# 수업 때만 True로 일단 설정하신 것임.
DEBUG = True

ALLOWED_HOSTS = [
    'eb-django-app-env.eba-ymwpwbwf.ap-northeast-2.elasticbeanstalk.com',
]

