$("#form_comment").on("submit", function (e) {

    e.preventDefault();


    var form = $('#form_comment')[0];

    // Create an FormData object 
    var formdata = new FormData(form);


    // It returns a array of object
    formdata.append('ajax', 'y');

    $.ajax({
        type: "POST",
        url: "{% url 'front_post_single_comment_submit' id=id %",
        data: formdata,
        processData: false,
        contentType: false,

        success: function (data) {
            if (data.success) {
                
                NioApp.Toast(data.message, 'success')

                $('#tableid2').append(tr)
                $('#dts_form_add').DataTable().ajax.reload();
                $('#myform2').trigger('reset').find('select').trigger('change');
                $('#build_forms').modal('hide');
            }
            else {
                
                NioApp.Toast(data.message, 'error')
            }
        }
    });
});