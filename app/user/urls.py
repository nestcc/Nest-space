"""
用于用户相关操作的urls
"""

from django.urls import path
from user.views import html as user_html
from user.views import json as user_json

paths = [path('login/', user_html.login, name='login'),
         path('submit_login/', user_json.log_in, name='submit_login'),

         path('user_list/', user_html.UserList.as_view()),
         path('user_detail/<int:user_id>/', user_html.UserDetail.as_view()),
         path('add_user/', user_html.AddUser.as_view()),
         path('del_user/', user_html.delet_user.as_view()),

         path('logout/', user_json.log_out, name='user_logout'),
         path('get_user_list/', user_json.get_user_list),
         path('upload_user_icon/<int:user_id>/', user_json.upload_user_icon),
         path('change_user_info/<int:user_id>/', user_json.change_user_info),
         path('change_pwd/<int:user_id>/', user_json.change_user_pwd),
         ]
