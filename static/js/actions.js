function Update() {


    var first_name = $('#first_name').val();
    var last_name = $('#last_name').val();
    var username = $('#username').val();
    var email = $('#email').val();
    var phone = $('#phone').val();
    var address = $('#address').val();
    var post_code = $('#post_code').val();

    $.get('update/', {

        first_name,
        last_name,
        username,
        email,
        post_code,
        address,
        phone,


    }).then(value => {
        $('#Information').html(value);
        const Toast = Swal.mixin({
            toast: true,
            position: 'top-end',
            showConfirmButton: false,
            timer: 3000,
            timerProgressBar: true,
            didOpen: (toast) => {
                toast.addEventListener('mouseenter', Swal.stopTimer)
                toast.addEventListener('mouseleave', Swal.resumeTimer)
            }
        })

        Toast.fire({
            icon: value.icon,
            title:value.title
        })
        // $('#Information').html();




    })
}