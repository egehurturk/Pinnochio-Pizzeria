document.addEventListener('DOMContentLoaded', ()=>{
    const dropdown = $('#myDropdown');
    const dropButton = $('.dropbtn');
    const closeButton = $('closeNotification');
    const notification = $('#notificationsLog')

    // By default, dropdown menu is closed
    dropdown.hide();

    // When the profile button is clicked, open the menu
    dropButton.click(()=> {
        dropdown.fadeToggle();
    });

    // When it is focused out, close the menu.
    dropButton.focusout(()=> {
        dropdown.fadeOut();
    });

    closeButton.click(()=> {
        console.log('clicked')
        notification.fadeOut();
    });


})
