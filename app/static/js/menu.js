/**Toggles the mobile menu in nav bar */

$(document).ready(function () {
    // Toggle the menu on clicking the hamburger button
    $('#menu-toggle').on('click', function () {
        $('#mobile-menu').toggleClass('hidden');
    });

    // Hide the menu when clicking on any link inside the menu
    $('#mobile-menu a').on('click', function () {
        $('mobile-menu').addClass('hidden');
    });

    // Hide the menu on click outside the menu
    $(document).on('click', function (e) {
        if (!$(e.target).closest('#mobile-menu, #menu-toggle').length) {
            $('#mobile-menu').addClass('hidden');
        }
    });
});