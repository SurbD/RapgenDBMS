function closeAlert() {
    flash_card = document.getElementById("flash-alert-id");

    if (flash_card === "none" ) {
        flash_card.style.display = "block"
    } else {
        flash_card.classList.add("close-animation")
        setTimeout(() => {
            flash_card.style.display = "none"
            flash_card.classList.remove("close-animation")
        }, 500)
        // window.location.href = "https://www.github.com/SurbD"; // Testing Redirect 
    }
}

function validateFileType() {
    var selectedFile = document.getElementById('fileInput').files[0];
    var allowedTypes = ['application/vnd.ms-excel', 'text/csv'];

    if (!allowedTypes.includes(selectedFile.type)) {
        console.log("Not a valid file type")
        // alert("Invalid file type. Please upload  a JPEG or PNG");
        document.getElementById("file-error-mssg").innerHTML = 'Invalid file type. Use your head.';
        document.getElementById('fileInput').value = '';
        // setTimeout(() => {
        //     document.getElementById('file-error-mssg').innerHTML = ''
        // }, 1000)
    } else {
        document.getElementById('file-error-mssg').innerText = '';
    }
}

// async function uploadFile() {
//     var filed = document.getElementById("fileInput").files[0];
//     console.log(filed);
//     
//     if (!filed) {
//         document.getElementById("file-error-mssg").innerHTML = 'File Input cannot be null.';
//         console.log("Emptyfield");
//         return false;
//     }
//     // var formData = new FormData();
//     // const dataFile = document.querySelector("#fileInput").files[0];
//     // formData.append('data', dataFile);
//     console.log("Got into uploadFile");
//
//     await axios.postForm('/upload-file', {
//         'file': document.querySelector("#fileInput").files[0]
//     });
// }

function fileUpload() {
    const file = document.getElementById("fileInput").files[0];
    console.log(file);

    if (!file) {
        document.getElementById("file-error-mssg").innerHTML = "Empty FileField";
        console.log('Empty Field Second Uploader');
        return false;
    }
    
    const promise = axios.postForm('/upload-file', {'file': file});
    const dataPromise = promise.then((response) => response.data);

    return dataPromise;
}

function uploadNow() {
    let message;
    
    fileUpload()
        .then(data => {
            console.log(data);
            message = data.result;

            console.log(message);
        })
        .catch(err => console.log(err))
    return message
}

function uploadFile() {
    let status = uploadNow();

    if (status == 'success') {
        console.log('Was SuccesFil');
    }
}

// function sendFormData() {
//     console.log('clicked Submit')
//     const form_data = document.forms['database-upload-form']
//     const data = {
//         first_name: form_data['firstName'].value,
//         last_name: form_data['lastName'].value,
//         email: form_data['email'].value,
//         phone_number: form_data['phoneNumber'].value,
//         date_of_birth: form_data['dateOfBirth'].value,
//         gender: form_data['gender'].value
//     }
//     console.log(data);
// }
