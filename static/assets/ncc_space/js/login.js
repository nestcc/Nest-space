layui.use('layer', function () {
    var layer = layui.layer;
});

function submit(url) {
    // layer.msg('ok');
    $.ajax({
        url: '/user/submit_login/',
        type: 'POST',
        cache: false,
        data: $('form').serialize(),
        success: function (data) {
            if (data['status'] === 'success') {
                layer.msg('success', {
                    time: 1000,
                    closeBtn: 1,
                    end: function () {
                        location.href = '/mana/index/';
                    }
                })
            } else {
                layer.msg(data['error'], {
                    time: 1000,
                    closeBtn: 1
                })
            }

        },
        error: function (error) {
            layer.msg('error', {
                time: 1000,
                closeBtn: 1
            })
        }
    })
}