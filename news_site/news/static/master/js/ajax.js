/* این فایل برای تمامی فرم های که در صفحه فرانت است استفاده می شود */
$("#form_all").on("submit", function (e) {
  e.preventDefault();
  var form = $('#form_all')[0];
  var formdata = new FormData(form);

  $.ajax({
      type: "POST",
      url: $('#form_all').attr('action'),
      data: formdata,
      processData: false,
      contentType: false,
      success: function (data) {
          console.log("پاسخ سرور:", data);
          if (data.success) {
              $('#category-table-body').load(window.location.href + ' #category-table-body > *');
              $('#form_all')[0].reset();
              $('#modal_category').modal('hide');
              toastr.options = {
                  timeOut: 2e3,
                  progressBar: !0,
                  showMethod: "slideDown",
                  hideMethod: "slideUp",
                  showDuration: 200,
                  hideDuration: 200,
                  positionClass: "toast-top-center"
              };
              toastr.success(data.message);
          } else {
              toastr.options = {
                  timeOut: 2e3,
                  progressBar: !0,
                  showMethod: "slideDown",
                  hideMethod: "slideUp",
                  showDuration: 200,
                  hideDuration: 200,
                  positionClass: "toast-top-center"
              };
              toastr.error(data.message);
          }
      },
      error: function(xhr, status, error) {
          console.error("خطا در درخواست:", xhr.responseText);
          toastr.options = {
              timeOut: 2e3,
              progressBar: !0,
              showMethod: "slideDown",
              hideMethod: "slideUp",
              showDuration: 200,
              hideDuration: 200,
              positionClass: "toast-top-center"
          };
          toastr.error("خطایی رخ داده است: " + error);
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




/* این فایل برای تمامی فرم های که در صفحه فرانت است استفاده می شود */
$("#sub_cat_add").on("submit", function (e) {
  e.preventDefault();
  var form = $('#sub_cat_add')[0];
  var formdata = new FormData(form);

  $.ajax({
      type: "POST",
      url: $('#sub_cat_add').attr('action'),
      data: formdata,
      processData: false,
      contentType: false,
      success: function (data) {
          console.log("پاسخ سرور:", data);
          if (data.success) {
              $('#sub-category-table-body').load(window.location.href + ' #sub-category-table-body > *');
              $('#sub_cat_add')[0].reset();
              $('#modal_sub_category_add').modal('hide');
              toastr.options = {
                  timeOut: 2e3,
                  progressBar: !0,
                  showMethod: "slideDown",
                  hideMethod: "slideUp",
                  showDuration: 200,
                  hideDuration: 200,
                  positionClass: "toast-top-center"
              };
              toastr.success(data.message);
          } else {
              toastr.options = {
                  timeOut: 2e3,
                  progressBar: !0,
                  showMethod: "slideDown",
                  hideMethod: "slideUp",
                  showDuration: 200,
                  hideDuration: 200,
                  positionClass: "toast-top-center"
              };
              toastr.error(data.message);
          }
      },
      error: function(xhr, status, error) {
          console.error("خطا در درخواست:", xhr.responseText);
          toastr.options = {
              timeOut: 2e3,
              progressBar: !0,
              showMethod: "slideDown",
              hideMethod: "slideUp",
              showDuration: 200,
              hideDuration: 200,
              positionClass: "toast-top-center"
          };
          toastr.error("خطایی رخ داده است: " + error);
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





$(document).ready(function() {
    $("[id^='form_reviwe_edit_']").on("submit", function (e) {
        e.preventDefault();
        var form = $(this)[0];
        var formdata = new FormData(form);

        $.ajax({
            type: "POST",
            url: $(this).attr('action'),
            data: formdata,
            processData: false,
            contentType: false,
            success: function (data) {
                console.log("پاسخ سرور:", data);
                if (data.success) {
                    $('#reviews-table-body').load(window.location.href + ' #reviews-table-body > *');
                    form.reset();
                    $(form).closest('.modal').modal('hide');
                    showToast(data.message, 'success');
                } else {
                    showToast(data.message, 'error');
                }
            },
            error: function(xhr, status, error) {
                console.error("خطا در درخواست:", xhr.responseText);
                showToast("خطایی رخ داده است: " + error, 'error');
            }
        });
    });

    function showToast(message, type) {
        toastr.options = {
            timeOut: 2000,
            progressBar: true,
            showMethod: "slideDown",
            hideMethod: "slideUp",
            showDuration: 200,
            hideDuration: 200,
            positionClass: "toast-top-center"
        };
        toastr[type](message);
    }
});






$(document).ready(function() {
    $("#addAuthorForm").on("submit", function (e) {
        e.preventDefault();
        submitAuthorForm();
    });
});

function submitAuthorForm() {
    var form = $('#addAuthorForm')[0];
    var formData = new FormData(form);

    $.ajax({
        type: "POST",
        url: form.action,
        data: formData,
        processData: false,
        contentType: false,
        success: function (response) {
            console.log("پاسخ سرور:", response);
            if (response.success) {
                updateAuthorTable();
                resetForm(form);
                closeModal();
                showToast('success', response.message);
            } else {
                showToast('error', response.message);
            }
        },
        error: function(xhr, status, error) {
            console.error("خطا در درخواست:", xhr.responseText);
            showToast('error', "خطایی رخ داده است: " + error);
        }
    });
}

function updateAuthorTable() {
    $('#author_table').load(window.location.href + ' #author_table > *', function() {
        // اینجا می‌توانید کدهای اضافی برای بعد از بارگذاری جدول اضافه کنید
    });
}

function resetForm(form) {
    form.reset();
}

function closeModal() {
    $('#AddAuthor_Modal').modal('hide');
    $('body').removeClass('modal-open');
    $('.modal-backdrop').remove();
}

function showToast(type, message) {
    toastr.options = {
        timeOut: 2000,
        progressBar: true,
        showMethod: "slideDown",
        hideMethod: "slideUp",
        showDuration: 200,
        hideDuration: 200,
        positionClass: "toast-top-center"
    };
    toastr[type](message);
}

