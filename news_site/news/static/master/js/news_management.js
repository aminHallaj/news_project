toastr.options = {
    timeOut: 2000,
    progressBar: true,
    showMethod: "slideDown",
    hideMethod: "slideUp",
    showDuration: 200,
    hideDuration: 200,
    positionClass: "toast-top-center"
};

document.addEventListener('DOMContentLoaded', function() {
    const approveBtn = document.getElementById('approveBtn');
    const rejectBtn = document.getElementById('rejectBtn');
    const rejectModal = new bootstrap.Modal(document.getElementById('rejectModal'));
    const rejectReasonInput = document.getElementById('rejectReason');

    window.approveNews = function(newsId) {
        setStatus(newsId, 1);
    };

    window.showRejectModal = function() {
        if (statusNews === 2) {
            rejectReasonInput.value = rejectReason;
        }
        rejectModal.show();
    };

    window.rejectNews = function(newsId) {
        const reason = rejectReasonInput.value.trim();
        if (reason === '') {
            toastr.error('لطفا دلیل رد خبر را وارد کنید.');
            return;
        }
        setStatus(newsId, 2, reason);
        rejectModal.hide();
        approveBtn.disabled = true;
        rejectBtn.textContent = 'ویرایش دلیل رد';
    };

    function setStatus(newsId, status, reason = '') {
        fetch(`/master/dashboard/post/change-status/${newsId}/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
            },
            body: new URLSearchParams({
                'status': status,
                'reason': reason
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                if (status === 1) {
                    toastr.success('خبر تایید شد.');
                    approveBtn.style.display = 'none';
                    rejectBtn.style.display = 'none';
                } else if (status === 2) {
                    toastr.warning('خبر رد شد.');
                    approveBtn.disabled = true;
                    rejectBtn.textContent = 'ویرایش دلیل رد';
                }
            } else {
                toastr.error('خطا در تغییر وضعیت خبر.');
            }
        })
        .catch(() => {
            toastr.error('خطا در ارتباط با سرور.');
        });
    }
});