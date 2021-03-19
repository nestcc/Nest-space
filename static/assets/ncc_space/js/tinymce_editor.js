tinymce.init({
    selector: '#article_content',
    statusbar: false,
    height: 600,
    plugins: 'image codesample',
    language: 'zh_CN',
    menubar: 'edit insert view format table tools help',
    toolbar: 'undo redo | styleselect numlist | bold italic | alignleft aligncenter alignright alignjustify | image codesample',
    file_picker_types: 'image',
    // images_upload_url: '/article/upload_article_image/',

    images_upload_handler: function (blobInfo, success, failure) {
        var image_form = new FormData();
        console.log(blobInfo.filename());
        image_form.append('image', blobInfo.blob(), blobInfo.filename());
        image_form.append('csrfmiddlewaretoken', $("input[name='csrfmiddlewaretoken']").val());
        console.log(image_form.keys());
        $.ajax({
            url: '/article/upload_article_image/',
            type: 'post',
            data: image_form,
            processData: false,
            contentType: false,
            success: function (data) {
                if (data['status'] === 'success') {
                    var origin_val = $("#img_set").val();
                    $("#img_set").val(origin_val + '|' + data['file_id']);
                    success(data.location);
                } else {
                    failure(data.error);
                }
            }
        })
    },

});