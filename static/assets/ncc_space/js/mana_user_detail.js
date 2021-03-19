var user_id = location.href.split('/')[5];
var csrf_token = $('input[name="csrfmiddlewaretoken"]').val();

layui.use(['upload', 'form'], function () {
    var upload = layui.upload;
    var form = layui.form;

    upload.render({
        elem: '#user-icon',
        url: '/mana/upload_user_icon/' + user_id + '/', //改成您自己的上传接口
        data: {'csrfmiddlewaretoken': csrf_token},
        accept: 'images',
        before: function (obj) {
            //预读本地文件示例，不支持ie8
            obj.preview(function (index, file, result) {
                $('#demo1').attr('src', result); //图片链接（base64）
            });
        },
        done: function (res) {
            //如果上传失败
            if (res['status'] === 'success') {
                layer.msg('上传成功', {
                    time: 1000,
                    closeBtn: 1,
                });
            } else {
                layer.msg(res['error'], {
                    closeBtn: 1
                })
            }
            //上传成功
        },
    });

    form.on('submit(submit-btn)', function (data) {
        $.ajax({
            url: location.href,
            type: 'POST',
            cache: false,
            data: $('#user_form').serialize(),
            success: function (data) {
                if (data['status'] === 'success') {
                    layer.msg('ok!!!', {
                        time: 1500,
                        closeBtn: 1,
                        end: function () {
                            location.reload();
                        }
                    })
                } else {
                    layer.open({
                        content: data['error'],
                        closeBtn: 1
                    })
                }
            }
        });
        return false;
    });

    form.on('submit(submit-pwd-btn)', function () {
        debugger;
        if ($('#pwd').val() !== $('#pwd_verify').val()) {
            layer.msg('两次密码不一致', {
                closeBtn: 1
            });
        } else {
            $.ajax({
                url: '/mana/change_pwd/' + user_id + '/',
                method: 'post',
                data: $('#pwd_form').serialize(),
                success: function (data) {
                    if (data['status'] === 'success') {
                        layer.msg('ok', {
                            time: 1500,
                            closeBtn: 1,
                            end: function () {
                                location.reload();
                            }
                        })
                    } else {
                        layer.msg(data['error'], {
                            closeBtn: 1
                        })
                    }
                }
            });
        }
        return false;
    });
});

