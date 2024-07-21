function del_category(id) {
  let row = $(`#row_${id}`);
  var csrftoken = $('[name=csrfmiddlewaretoken]').val();
  swal({
    title: "مطمئن هستید؟",
    text: "در صورت پاک کردن فایل نمیتوانید به آن دسترسی داشته باشید",
    icon: "warning",
    buttons: {
      cancel: "انصراف",
      confirm: "بله، حذف کن"
    },
    buttons: true,
    dangerMode: true,
  }).then((willDelete) => {
    if (willDelete) {
      $.ajax({
        type: "POST",
        url: `/master/dashboard/category/delete/${id}/`,
        data: { id },
        headers: { 
          'X-CSRFToken': csrftoken
        },
        success: function (data) {
          row.remove();
          $(`#del_${id}`).remove();
          console.log(data);
        }
      });
      //alert();
      swal(" دسته بندی با موفقیت حذف شد. ", {
        icon: "success",
      });
    }
    else {
      swal("دسته بندی هنوز وجود دارد !", {
        icon: "error",
      });
    }
  });
}




function del_news(id) {
  let row = $(`#row_${id}`);
  var csrftoken = $('[name=csrfmiddlewaretoken]').val();
  swal({
    title: "مطمئن هستید؟",
    text: "در صورت پاک کردن خبر نمیتوانید به آن دسترسی داشته باشید",
    icon: "warning",
    buttons: {
      cancel: "انصراف",
      confirm: "بله، حذف کن"
    },
    buttons: true,
    dangerMode: true,
  }).then((willDelete) => {
    if (willDelete) {
      $.ajax({
        type: "POST",
        url: `/master/dashboard/post/delete/${id}/`,
        data: { id },
        headers: { 
          'X-CSRFToken': csrftoken
        },
        success: function (data) {
          row.remove();
          $(`#del_${id}`).remove();
          console.log(data);
        }
      });
      //alert();
      swal(" خبر با موفقیت حذف شد. ", {
        icon: "success",
      });
    }
    else {
      swal("خبر هنوز وجود دارد !", {
        icon: "error",
      });
    }
  });
}
