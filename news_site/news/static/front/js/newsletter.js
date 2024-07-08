$(document).ready(function() {
  $('#newsletter-form').submit(function(event) {
      event.preventDefault();

      var formData = $(this).serialize();

      $.ajax({
          type: 'POST',
          url: "/post/news/letters/add/submit/",
          data: formData,
          success: function(response) {
              if (response.success) {
                toastr.options = {
                  timeOut: 2e3,
                  progressBar: !0,
                  showMethod: "slideDown",
                  hideMethod: "slideUp",
                  showDuration: 200,
                  hideDuration: 200,
                  positionClass: "toast-top-center"
                }
                  toastr.success(response.message);
                  $('#newsletter-form')[0].reset();
              } else {
                toastr.options = {
                  timeOut: 2e3,
                  progressBar: !0,
                  showMethod: "slideDown",
                  hideMethod: "slideUp",
                  showDuration: 200,
                  hideDuration: 200,
                  positionClass: "toast-top-center"
                }
                  toastr.error(response.message);
              }
          },
          error: function(xhr, status, error) {
              toastr.error('An error occurred: ' + error);
          }
      });
  });
});



$(document).ready(function() {
  $('#newsletter-form2').submit(function(event) {
      event.preventDefault();

      var formData = $(this).serialize();

      $.ajax({
          type: 'POST',
          url: "/post/news/letters/add/submit/",
          data: formData,
          success: function(response) {
              if (response.success) {
                toastr.options = {
                  timeOut: 2e3,
                  progressBar: !0,
                  showMethod: "slideDown",
                  hideMethod: "slideUp",
                  showDuration: 200,
                  hideDuration: 200,
                  positionClass: "toast-top-center"
                }
                  toastr.success(response.message);
                  $('#newsletter-form')[0].reset();
              } else {
                toastr.options = {
                  timeOut: 2e3,
                  progressBar: !0,
                  showMethod: "slideDown",
                  hideMethod: "slideUp",
                  showDuration: 200,
                  hideDuration: 200,
                  positionClass: "toast-top-center"
                }
                  toastr.error(response.message);
              }
          },
          error: function(xhr, status, error) {
              toastr.error('An error occurred: ' + error);
          }
      });
  });
});