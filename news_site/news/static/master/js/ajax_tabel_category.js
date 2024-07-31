$(document).ready(function() {
  // صفحه‌بندی
  $(document).on('click', '#category-pagination a', function(e) {
      e.preventDefault();
      var page_url = $(this).attr('href');
      if (page_url) {
          loadCategoryTable(page_url + '&table=category');
      }
  });

  // جستجو
  $('#category-search-input').on('keyup', function() {
      var search = $(this).val();
      var url = $('#category-search-form').attr('action') + '?category_search=' + search + '&table=category';
      loadCategoryTable(url);
  });

  function loadCategoryTable(url) {
      $.ajax({
          url: url,
          type: 'get',
          dataType: 'json',
          success: function(data) {
              $('#category-table-body').html(data.html_from_view);
              $('#category-pagination').html(data.pagination_html);
              history.pushState(null, '', url);
              updateCategoryItemCountText(data.start_index, data.end_index, data.total_count);
          }
      });
  }

  function updateCategoryItemCountText(start, end, total) {
      var text = 'نمایش ' + start + ' تا ' + end + ' از ' + total;
      $('#category-item-count').text(text);
  }
});