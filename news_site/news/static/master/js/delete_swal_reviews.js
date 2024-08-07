function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}

function del_reviews(id) {
  let row = $(`#row_${id}`);
  const csrftoken = getCookie('csrftoken');
  swal({
    title: "مطمئن هستید؟",
    text: "با حذف نظر کاربر دیگر به نظر کاربر دسترسی ندارید!",
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
        url: `/master/dashboard/reviews/delete/${id}/`,
        data: { id },
        headers: {
          "X-CSRFToken": csrftoken
        },
        success: function (data) {
          row.remove();
          $(`#del_${id}`).remove();
          console.log(data);
        }
      });
      //alert();
      swal(" نظر کاربر با موفقیت حذف شد. ", {
        icon: "success",
      });
    }
    else {
      swal("نظر کاربر هنوز وجود دارد !", {
        icon: "error",
      });
    }
  });
}





function del_sub_category(id) {
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
        url: `/master/dashboard/sub/category/delete/${id}/`,
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
      swal(" زیرمجوعه با موفقیت حذف شد. ", {
        icon: "success",
      });
    }
    else {
      swal("زیرمجوعه هنوز وجود دارد !", {
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
