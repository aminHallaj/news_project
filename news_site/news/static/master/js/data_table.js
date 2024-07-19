let dt_news;
	$(document).ready(function () {
		dt_news = $('#dt_news').DataTable({
			
			processing: true,
			serverSide: true,
			paging: true,
			responsive: true,
			searching: true,

			ajax: {
				type: "POST",
				url: "{% url 'test_datatable' %}",
				headers: { 'X-CSRFToken': '{{ csrf_token }}' },
			},
			columns: [
				{ data: 'title' },
				
			],
		});
	});