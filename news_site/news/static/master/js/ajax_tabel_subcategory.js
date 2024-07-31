$(document).ready(function() {
  // صفحه‌بندی
  $(document).on('click', '#subcategory-pagination a', function(e) {
      e.preventDefault();
      var page_url = $(this).attr('href');
      if (page_url) {
          loadSubcategoryTable(page_url + '&table=subcategory');
      }
  });

  // جستجو
  $('#subcategory-search-input').on('keyup', function() {
      var search = $(this).val();
      var url = $('#subcategory-search-form').attr('action') + '?subcategory_search=' + search + '&table=subcategory';
      loadSubcategoryTable(url);
  });

  function loadSubcategoryTable(url) {
      $.ajax({
          url: url,
          type: 'get',
          dataType: 'json',
          success: function(data) {
              $('#sub-category-table-body').html(data.html_from_view);
              $('#subcategory-pagination').html(data.pagination_html);
              history.pushState(null, '', url);
              updateSubcategoryItemCountText(data.start_index, data.end_index, data.total_count);
          }
      });
  }

  function updateSubcategoryItemCountText(start, end, total) {
      var text = 'نمایش ' + start + ' تا ' + end + ' از ' + total;
      $('#subcategory-item-count').text(text);
  }
});