$(document).ready(function() {
  // صفحه‌بندی
  $(document).on('click', '#author-pagination a', function(e) {
      e.preventDefault();
      var page_url = $(this).attr('href');
      if (page_url) {
          loadAuthorTable(page_url + '&table=author');
      }
  });

  // جستجو
  $('#author-search-input').on('keyup', function() {
      var search = $(this).val();
      var url = $('#author-search-form').attr('action') + '?author_search=' + search + '&table=author';
      loadAuthorTable(url);
  });

  function loadAuthorTable(url) {
      $.ajax({
          url: url,
          type: 'get',
          dataType: 'json',
          success: function(data) {
              $('#author-table-body').html(data.html_from_view);
              $('#author-pagination').html(data.pagination_html);
              history.pushState(null, '', url);
              updateAuthorItemCountText(data.start_index, data.end_index, data.total_count);
          }
      });
  }

  function updateAuthorItemCountText(start, end, total) {
      var text = 'نمایش ' + start + ' تا ' + end + ' از ' + total;
      $('#author-item-count').text(text);
  }
});