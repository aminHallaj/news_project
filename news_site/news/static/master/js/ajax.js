/* این فایل برای تمامی فرم های که در صفحه فرانت است استفاده می شود */

$("#form_all").on("submit", function (e) {
    e.preventDefault();
    var form = $('#form_all')[0];
    // Create an FormData object 
    var formdata = new FormData(form);
    console.log(formdata);

    $.ajax({
      type: "POST",
      url: $('#form_all').attr('action'),
      data: formdata,
      processData: false,
      contentType: false,

      success: function (data) {
        if (data.success) {
          toastr.options = {
            timeOut: 2e3,
            progressBar: !0,
            showMethod: "slideDown",
            hideMethod: "slideUp",
            showDuration: 200,
            hideDuration: 200,
            positionClass: "toast-top-center"
          }
        $('#all-section').load(window.location.href + ' #all-section > *');
        toastr.success(data.message)
        $('#form_all')[0].reset();

        // بستن مودال
        $('#modal_category').modal('hide');

        }
        else {
          toastr.options = {
            timeOut: 2e3,
            progressBar: !0,
            showMethod: "slideDown",
            hideMethod: "slideUp",
            showDuration: 200,
            hideDuration: 200,
            positionClass: "toast-top-center"
          }
          toastr.error(data.message)
        }
      }
    });
  });









  $("#form_post_edit").on("submit", function (e) {
    e.preventDefault();
    var form = $('#form_post_edit')[0];
    var formdata = new FormData(form);

    $.ajax({
        type: "POST",
        url: $(this).attr('action'),
        data: formdata,
        processData: false,
        contentType: false,
        success: function (data) {
            if (data.success) {
                toastr.success(data.message, '', {
                    timeOut: 2e3,
                    progressBar: true,
                    showMethod: "slideDown",
                    hideMethod: "slideUp",
                    showDuration: 200,
                    hideDuration: 200,
                    positionClass: "toast-top-center"
                });
                window.location.href = data.redirect_url;
            } else {
                toastr.error(data.message, '', {
                    timeOut: 2e3,
                    progressBar: true,
                    showMethod: "slideDown",
                    hideMethod: "slideUp",
                    showDuration: 200,
                    hideDuration: 200,
                    positionClass: "toast-top-center"
                });
            }
        },
        error: function (xhr, status, error) {
            toastr.error("An error occurred: " + error, '', {
                timeOut: 2e3,
                progressBar: true,
                showMethod: "slideDown",
                hideMethod: "slideUp",
                showDuration: 200,
                hideDuration: 200,
                positionClass: "toast-top-center"
            });
        }
    });
});

















$("#form_category_edit").on("submit", function (e) {
  e.preventDefault();
  var form = $('#form_category_edit')[0];
  // Create an FormData object 
  var formdata = new FormData(form);
  console.log(formdata);

  $.ajax({
    type: "POST",
    url: $('#form_category_edit').attr('action'),
    data: formdata,
    processData: false,
    contentType: false,

    success: function (data) {
      if (data.success) {
        toastr.options = {
          timeOut: 2e3,
          progressBar: !0,
          showMethod: "slideDown",
          hideMethod: "slideUp",
          showDuration: 200,
          hideDuration: 200,
          positionClass: "toast-top-center"
        }
      $('#all-section').load(window.location.href + ' #all-section > *');
      toastr.success(data.message)
      // $('#form_category_edit')[0].reset();

      // بستن مودال
      $('.modal').modal('hide');

      }
      else {
        toastr.options = {
          timeOut: 2e3,
          progressBar: !0,
          showMethod: "slideDown",
          hideMethod: "slideUp",
          showDuration: 200,
          hideDuration: 200,
          positionClass: "toast-top-center"
        }
        toastr.error(data.message)
      }
    }
  });
});

