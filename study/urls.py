from django.urls import path
from .views import *

app_name = "study"
urlpatterns = [
    path("", studylist, name="studylist"),  # 스터디 목록 페이지
    path("new/", new, name="new"),  # 새 스터디 생성 페이지
    path("create/", create, name="create"),  # 새 스터디 생성 동작
    path("<int:id>/", detail, name="detail"),  # 스터디 상세 페이지
    path("edit/<int:id>", edit, name="edit"),  # 기존 스터디 수정 페이지
    path("update/<int:id>", update, name="update"),  # 기존 스터디 수정 동작
    path("delete/<int:id>", delete, name="delete"),  # 기존 스터디 삭제 동작
    path("apply/<int:id>", apply_study, name="apply_study"),  # 스터디 가입 신청
    path(
        "accept_request/<int:study_id>/<int:user_id>",
        accept_request,
        name="accept_request",
    ),  # 스터디 가입 승인 동작
    path(
        "refuse_request/<int:study_id>/<int:user_id>",
        refuse_request,
        name="refuse_request",
    ),  # 스터디 가입 거절 동작
    path("over/<int:id>", recruit_over, name="recruit_over"),  # 스터디 마감으로 전환 동작
]