/**Handles login with firebase */

// Import functions needed from CDN/SDKs
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.12.0/firebase-app.js"
import { getAuth, GoogleAuthProvider, signInWithPopup } from "https://www.gstatic.com/firebasejs/9.12.0/firebase-auth.js"


$(document).ready(function() {
    // Firebase Config
    const firebaseConfig = {
        apiKey: "AIzaSyB4TWHVtzuG0wShdoTJ4j3RDy_h36icm4M",
        authDomain: "linkit-9f900.firebaseapp.com",
        projectId: "linkit-9f900",
        storageBucket: "linkit-9f900.firebasestorage.app",
        messagingSenderId: "572567854894",
        appId: "1:572567854894:web:bf8deb7c83b137bf01a4bf"
    };

    // Initialize Firebase
    const app = initializeApp(firebaseConfig);

    // Initialize Firebase Auth
    const auth = getAuth(app);
    const provider = new GoogleAuthProvider();

    $('#google-login-btn').on('click', function() {
        signInWithPopup(auth, provider)
            .then(function(result) {
                // Get the ID token from the result
                result.user.getIdToken().then(function(idToken) {
                    // Send token to Flask backend using Ajax
                    $.ajax({
                        url: '/auth/login',
                        type: 'POST',
                        contentType: 'application/json',
                        data: JSON.stringify({ id_token: idToken }),
                        success: function(response) {
                            if (response.status === 'success') {
                                $('#login-modal').removeClass('flex').addClass('hidden')

                                const savedForm = localStorage.getItem('savedFormData')
                                if (savedForm) {
                                    const formObj = JSON.parse(savedForm)
                                    const newFormData = new FormData()
                                    for (const key in formObj) {
                                        newFormData.append(key, formObj[key])
                                    }

                                    $.ajax({
                                        url: '/submit',
                                        method: 'POST',
                                        data: newFormData,
                                        processData: false,
                                        contentType: false,
                                        success: function(response) {
                                            alert(response.message)
                                            localStorage.removeItem('savedFormData')
                                            $('#url-form')[0].reset()
                                        },
                                        error: function (xhr) {
                                            alert('form submission failed after login!')
                                        }
                                    })
                                }
                            }
                        }
                    })
                })
            })
    })
      
})