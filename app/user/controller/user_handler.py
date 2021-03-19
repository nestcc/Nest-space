from user.models import NepUser
from django.contrib.auth.models import Group


def get_ulist_with_var(page, limit, group):
    u_list = NepUser.objects.all().order_by('id')[(page - 1) * limit: page * limit]
    u_list_at_page = []
    for each_user in u_list:
        # print(each_user.icon.url)
        u_list_at_page.append({
            'id': each_user.id,
            'name': each_user.username,
            'mobile': each_user.mobile,
            'email': each_user.email,
            'group': each_user.groups.name,
            'join_time': each_user.date_joined,
            'last_time': each_user.last_login,
            'active': each_user.is_active
        })
    return u_list_at_page


def handle_upload_user_icon(icon, user_id):
    icon_user = NepUser.objects.get(pk=user_id)
    if icon_user.icon.url != 'user_icon/default-icon.jpg':
        icon_user.icon.delete()
    icon_user.icon = icon
    try:
        icon_user.save()
        return {'status': 'success',
                'icon_path': icon_user.icon.url}
    except Exception as any_exec:
        return {'status': 'fail',
                'error': repr(any_exec)}


def handle_change_user_info(request, user_id):
    user_obj = NepUser.objects.get(pk=user_id)
    user_obj.username = request.POST['username']
    user_obj.email = request.POST['email']
    user_obj.mobile = request.POST['mobile']
    user_obj.last_name = request.POST['lastname']
    user_obj.first_name = request.POST['firstname']

    try:
        user_obj.save()
        return {'status': 'success'}
    except Exception as any_exec:
        return {'status': 'fail',
                'error': repr(any_exec)}


def handle_change_pwd(user_id, pwd):
    user_obj = NepUser.objects.get(pk=user_id)
    user_obj.set_password(pwd)
    try:
        user_obj.save()
        return {'status': 'success'}
    except Exception as any_exec:
        return {'status': 'fail',
                'error': repr(any_exec)}


def handle_add_user(user_dict):
    try:
        new_user = NepUser.objects.create_user(username=user_dict['username'],
                                               email=user_dict['email'],
                                               mobile=user_dict['mobile'],
                                               last_name=user_dict['lastname'],
                                               first_name=user_dict['firstname'],
                                               password=user_dict['pwd'])
        new_user.groups.add(Group.objects.get(name='normal_user'))
        new_user.save()

        return {'status': 'success'}
    except Exception as any_exec:
        return {'status': 'fail',
                'error': repr(any_exec)}


def handle_del_user(user_id):
    del_user = NepUser.objects.get(pk=user_id)
    try:
        del_user.delete()
        return {'status': 'success'}
    except Exception as any_exec:
        return {'status': 'fail',
                'error': repr(any_exec)}
