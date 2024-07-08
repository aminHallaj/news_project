document.addEventListener('DOMContentLoaded', function() {
	const loadMoreCategoriesButton = document.getElementById('load-more-categories');
	const categoryContainer = document.getElementById('category-container');
	const categoryItems = categoryContainer.querySelectorAll('.category-item');
	let currentIndex = 0;
	const itemsPerPage = 2;
  
	// ابتدا تمام دسته‌ها را مخفی کنید
	categoryItems.forEach(item => item.style.display = 'none');
  
	// تابع برای نمایش دسته‌ها
	function showCategoryItems() {
	  const maxIndex = currentIndex + itemsPerPage;
	  for (let i = currentIndex; i < maxIndex && i < categoryItems.length; i++) {
		categoryItems[i].style.display = 'block';
	  }
	  currentIndex = maxIndex;
  
	  // اگر همه دسته‌ها نمایش داده شدند، دکمه را غیرفعال کنید
	  if (currentIndex >= categoryItems.length) {
		loadMoreCategoriesButton.disabled = true;
	  }
	}
  
	// نمایش دسته‌های اولیه
	showCategoryItems();
  
	// رویداد کلیک روی دکمه
	loadMoreCategoriesButton.addEventListener('click', showCategoryItems);
  });