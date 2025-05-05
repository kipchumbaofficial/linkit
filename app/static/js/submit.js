/** Handles link submissions for Shortening and saving
 *  Also  Checks if user is signed in and prompts them if not
 */
$(document).ready(function () {
    // Submit button clicked
    $('#url-form').on('submit', function (event) {
        event.preventDefault()

        const formData = new FormData(this)
        const formObj = {}
        formData.forEach((value, key) => {
            formObj[key] = value
        }) 
        // Save the serialized form data into localStorage
        localStorage.setItem('savedFormData', JSON.stringify(formObj))

        // Disable the submit button
        $('#submit-btn').prop('disabled', true)

        // Button UI
        $('.button-text').addClass('invisible')
        $('.spinner').removeClass('hidden')

        // Check login status of current user 
        $.ajax({
            url: '/submit',
            method: 'POST',
            data: formData,
            processData: false,
            contentType: false,
            success: function (response) {
               alert(response.message);
               localStorage.removeItem('savedFormData')
               $('#url-form')[0].reset()
            },
            error: function (xhr) {
                if (xhr.status === 401) {
                    $('#login-modal').removeClass('hidden').addClass('flex')
                }
            },
            complete: function () {
                // Re-enable the button after request finish
                $('#submit-btn').prop('disabled', false)

                // Button UI
                $('.button-text').removeClass('invisible')
                $('.spinner').addClass('hidden')
            }
        })
    })
})