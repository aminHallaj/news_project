let dt_list_post;
$(document).ready(function () {
		dt_list_post = $('#dt_news').DataTable({
			"language": {
				url: 'http://cdn.datatables.net/plug-ins/1.13.2/i18n/fa.json'
			},
			processing: true,
			serverSide: true,
			paging: true,
			responsive: true,
			searching: true,
            
			ajax: {
				type: "POST",
				url: "{% url 'master_post_list_datatable' %}",
				headers: { 'X-CSRFToken': '{{ csrf_token }}' },
			},
			columns: [
				{ data: 'id' },
				{ data: 'title' },
				{ data: 'author' },
				{ data: 'sub_category' },
				{ data: 'date' },
                { data:'<button>فعالیت</button>' },
				
				
			],
			// createdRow: function (row, data, index) {
			// 	let cls = "table-warning";
			// 	if (data.active_send_form==3) {
			// 		cls = "table-success";
			// 	}
			// 	else if (data.active_send_form==0) {
			// 		cls = "table-warning";
			// 	}
			// 	else if (data.active_send_form==2) {
			// 		cls = "table-danger";
			// 	}
			// 	$('td', row).eq(5).addClass(cls);
			// },
		});
	});