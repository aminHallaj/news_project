    const loadMoreButton = document.getElementById('load-more');
		const newsContainer = document.getElementById('news-container');
		const newsItems = newsContainer.querySelectorAll('.news-item');
		let currentIndex = 0;
		const itemsPerPage = 6; // تعداد خبرهایی که می‌خواهید در هر صفحه نمایش دهید

		// ابتدا تمام خبرها را مخفی کنید
		newsItems.forEach(item => item.style.display = 'none');

		// تابع برای نمایش خبرها
		function showNewsItems() {
			const maxIndex = currentIndex + itemsPerPage;
			for (let i = currentIndex; i < maxIndex && i < newsItems.length; i++) {
				newsItems[i].style.display = 'block';
			}
			currentIndex = maxIndex;

			// اگر همه خبرها نمایش داده شدند، دکمه را غیرفعال کنید
			if (currentIndex >= newsItems.length) {
				loadMoreButton.disabled = true;
			}
		}

		// نمایش خبرهای اولیه
		showNewsItems();

		// رویداد کلیک روی دکمه
		loadMoreButton.addEventListener('click', showNewsItems);



		