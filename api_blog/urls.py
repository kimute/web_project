from rest_framework import routers
from .views import UserViewSet, EntryViewSet


# routerを使ってModelを毎に登録
# GET /api/user: userの一覧
# GET /api/entries: Entryの一覧ができる
router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('entries', EntryViewSet)
