      // checking username with ajax 
      let usernamevalid = true;
      function checkUsernameAvailability() {
            const username = document.getElementById("username").value;
            const usernameMessage = document.getElementById("usernameMessage");

            if (username.length < 3) {
                usernameMessage.textContent = 'Username is too short.';
                usernameMessage.style.color='red';
                usernamevalid = false;
                return;
            }

            // Make an AJAX request to check username availability
            const xhr = new XMLHttpRequest();
            xhr.open('GET', `/check_username/?username=${username}`, true);

            xhr.onreadystatechange = function () {
                if (xhr.readyState === 4) {
                    if (xhr.status === 200) {
                        const data = JSON.parse(xhr.responseText);
                        if (data.exists) {
                            usernameMessage.textContent = 'Username is already taken.';
                            usernameMessage.style.color='red';
                            usernamevalid = false;
                            // console.log(usernamevalid);
                        } else {
                            usernameMessage.textContent = 'Username is available.';
                            usernameMessage.style.color='green';
                            usernamevalid = true;
                            // console.log(usernamevalid);
                        }
                    } else {
                        console.error('An error occurred:', xhr.status, xhr.statusText);
                        usernameMessage.textContent = 'Error checking username availability.';
                    }
                }
            };

            xhr.send();
      }     
      // checking email validity 
      let emailvalidity = true;
      function checkEmail(){
        let email = document.getElementById('email').value;
        let emailError = document.getElementById('emailError');
        let emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
          if(!email.match(emailRegex)) {
              emailError.textContent = "Please enter a valid email address.";
              emailError.style.color = 'red';
              emailvalidity=false;
          }else{
              emailError.textContent = "valid email adress";
              emailError.style.color = 'green';
              emailvalidity=true;
          }
        }
        // checking password validity 
        let passwordvalidity = true;
        function checkPassword(){
          let password = document.getElementById("password").value;
          let passwordError = document.getElementById("passwordError");         
          if(password.length<5){
              passwordError.textContent = "password must be 5 characters long";
              passwordError.style.color = "red";
              passwordvalidity=false;
          }else{
              passwordError.textContent = "password is valid";
              passwordError.style.color = "green";
              passwordvalidity = true;
          }
        }
        let passwordEquality = true;
        function checkPasswordEqual(){
              let pasword = document.getElementById("password");
              let confirmPassword = document.getElementById("confirmPassword");
              if((password.value.length < 5) || (password.value !== confirmPassword.value)){
                  confirmPassword.style.backgroundColor="red";
                  passwordEquality=false;
              }else{
                  confirmPassword.style.backgroundColor="green";
                  passwordEquality=true;
              }
        }
        // form validating 
        function validateForm(){
          let agree = document.getElementById("agree").checked;
          let valid = usernamevalid && emailvalidity && passwordvalidity && passwordEquality && agree;
          if(!valid){
            window.alert('please fill out the form correctly');
          }
          return valid;
        }