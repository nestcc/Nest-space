var laytable = '';
var csrf_token = $("input[name='csrfmiddlewaretoken']").val();

layui.use(['laydate', 'table'], function () {
    laytable = layui.table;

    laytable.render({
        elem: '#user_table',
        id: 'user_table',
        url: '/user/get_user_list/',
        limit: 10,
        page: {
            layout: ['count', 'prev', 'page', 'next', 'skip'],
        },
        cols: [[
            // {checkbox: true, width: 40},
            {field: 'id', width: 80, fixed: 'left', title: 'ID'},
            {field: 'name', width: 200, title: '用户名'},
            {field: 'mobile', width: 200, title: '电话'},
            {field: 'email', width: 200, title: '邮箱'},
            {field: 'group', width: 150, title: '用户组'},
            {field: 'join_time', width: 200, title: '加入时间'},
            {field: 'last_time', width: 200, title: '最后登录时间'},
            {field: 'active', width: 200, title: '人员状态'},
            {fixed: 'right', width: 120, align: 'center', title: '操作', toolbar: '#tool-bar'}
        ]]
    })

    // laytable.on('row(user_table)', function (obj) {
    //     layer.open({
    //         type: 2,
    //         shadeClose: true,
    //         resize: true,
    //         area: ['1000px', '700px'],
    //         content: '/mana/user_detail/' + obj.data['id'] + '/',
    //         closeBtn: 1,
    //         end: reload
    //     });
    // });

    laytable.on('tool(user_table)', function (obj) {
        if (obj.event === 'edit') {
            layer.open({
                type: 2,
                shadeClose: true,
                resize: true,
                area: ['1000px', '700px'],
                content: '/user/user_detail/' + obj.data['id'] + '/',
                closeBtn: 1,
                end: reload()
            });
        } else if (obj.event === 'unavai') {
            layer.confirm('还未实现哦')
        } else if (obj.event === 'del') {
            layer.confirm('确认要删除用户' + obj.data['name'] + '吗？',
                {title: '提示'},
                function () {
                    $.ajax({
                        url: '/user/del_user/',
                        type: 'post',
                        data: {
                            'csrfmiddlewaretoken': csrf_token,
                            'user_id': obj.data['id'],
                        },
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


function add_user() {
    layer.open({
        type: 2,
        shadeClose: true,
        resize: true,
        area: ['1000px', '700px'],
        content: '/user/add_user/',
        closeBtn: 1,
        end: reload
    })
}

function reload() {
    console.log('reload');
    laytable.reload('user_table');
}
