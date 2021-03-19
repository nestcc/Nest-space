layui.use(['layer', 'form'], function () {
    var layer = layui.layer;
    var layform = layui.form;

    layform.on('submit(submit-btn)', function (data) {
        $.ajax({
            url: '/user/add_user/',
            type: 'post',
            data: $("#add_form").serialize(),
            success: function (data) {
                if (data['status'] === 'success') {
                    layer.msg('ok', {
                        time: 1500,
                        closeBtn: 1,
                    });
                } else {
                    layer.msg(data['error'], {
                        closeBtn: 1
                    })
                }
            },
            error: function (xhr) {
                layer.msg('error', {
                    closeBtn: 1
                })
            }
        });
        return false;
    });
});