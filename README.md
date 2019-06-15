# Django Rest FrameWork
### ● Django REST Frameworkを使っAPIを作成
### ● WEBコンソールが付けているのでAPIの動作確認が簡単にできる
### ● コンソールを使用することでJSONを見やすく表示できたり、APIをテストするためのフォームを自前で用意する必要がない
# 確認環境
### ・OS:mac Mojave
### ・Python:3.6
### ・Django:2.2
### ・djangorestframework: 3.3.1
# Model
### api_blog/models.py
### 自分で定義したモデルを追加
### (追加されていることをDjango administrationで確認する)
## class user
###   name 
###   e-mail
## class Entry
###    記事を表示
## settings.pyにapi_blogを登録
## 動作確認(rest apiを組む前に実施)

# admin用
 
    python manage.py　createsuperuser
    python manage.py runserver

# Serializer

### field : APIとして出力したいフィールドname,mail

# ViewSet
### class UserViewset
###    
