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
        // $('#start-cart').load(window.location.href + ' #start-cart');
        toastr.success(data.message)
        $('#form_all')[0].reset();

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

