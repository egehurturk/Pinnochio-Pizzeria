

document.addEventListener('DOMContentLoaded', ()=> {
    const notification = $('#notificationsLog')
    $('closeNotification').click(()=>{
        notification.fadeOut()
    })
})
