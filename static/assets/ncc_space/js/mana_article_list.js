var laytable = '';
var csrf_token = $("input[name='csrfmiddlewaretoken']").val();

layui.use(['laydate', 'table'], function () {
    laytable = layui.table;

    laytable.render({
        elem: '#article_table',
        id: 'article_table',
        url: '/article/get_article_list/',
        limit: 10,
        page: {
            layout: ['count', 'prev', 'page', 'next', 'skip'],
        },
        cols: [[
            // {checkbox: true, width: 40},
            {field: 'id', width: 80, fixed: 'left', title: 'ID'},
            {field: 'title', width: 200, title: '文章名'},
            {field: 'subtitle', width: 200, title: '副标题'},
            {field: 'auth', width: 200, title: '作者'},
            {field: 'category', width: 150, title: '分类'},
            {field: 'create_time', width: 200, title: '创建日期'},
            {field: 'update_time', width: 200, title: '更新日期'},
            {field: 'view_time', width: 200, title: '查看次数'},
            {fixed: 'right', width: 180, align: 'center', title: '操作', toolbar: '#tool-bar'}
        ]]
    })

    laytable.on('tool(article_table)', function (obj) {
        if (obj.event === 'edit') {
            layer.open({
                type: 2,
                shadeClose: true,
                resize: true,
                area: ['1000px', '700px'],
                content: '/article/article_detail/' + obj.data['id'] + '/',
                closeBtn: 1,
                end: reload()
            });
        } else if (obj.event === 'unavai') {
            layer.confirm('还未实现哦')
        } else if (obj.event === 'del') {
            layer.confirm('确认要删除文章' + obj.data['name'] + '吗？',
                {title: '提示'},
                function () {
                    $.ajax({
                        url: '/article/del_article/' + obj.data['id'] + '/',
                        type: 'get',
                        // data: {
                        //     'csrfmiddlewaretoken': csrf_token,
                        //     'user_id': obj.data['id'],
                        // },
                        success: function (data) {
                            if (data['status'] === 'success') {
                                layer.msg('ok!!!', {
                                    time: 1500,
                                    closeBtn: 1,
                                    end: reload()
                                })
                            } else {
                                layer.msg(data['error'], {
                                    time: 1500,
                                    closeBtn: 1
                                })
                            }
                        }
                    });
                })
        }
    });
});

function reload() {
    console.log('reload');
    laytable.reload('article_table');
}
