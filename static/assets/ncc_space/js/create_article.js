layui.use(['layer', 'form'], function () {
    var layer = layui.layer;
    var layform = layui.form;
    // var $ = layui.jquery;

    layform.on('submit(submit-btn)', function (data) {
        tinyMCE.editors['article_content'].save();
        $.ajax({
            url: '/article/create_article/',
            type: 'post',
            data: $("#create-article-form").serialize(),
            success: function (data_return) {
                if (data_return['status'] === 'success') {
                    layer.msg('创建成功！！！', {
                        time: 1500,
                        closeBtn: 1
                    })
                } else {
                    layer.alert(data_return['error'], {
                        time: 0,
                        closeBtn: 1
                    })
                }
            }
        });
        return false;
    });
});