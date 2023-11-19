function closeAlert() {
    flash_card = document.getElementById("flash-alert-id");

    if (flash_card === "none" ) {
        flash_card.style.display = "block"
    } else {
        flash_card.classList.add("close-animation")
        setTimeout(() => {
            flash_card.style.display = "none"
            flash-card.classList.remove("close-animation")
        }, 500)
        // window.location.href = "https://www.github.com/SurbD"; // Testing Redirect 
    }
}

function validateFileType() {
    var selectedFile = document.getElementById('file-input').files[0];
    var allowedTypes = ['image/jpeg', 'image/png'];

    if (!allowedTypes.includes(selectedFile.type)) {
        // alert("Invalid file type. Please upload  a JPEG or PNG");
        document.getElementById("file-error-mssg").innerHTML = 'Invalid file type. Use your head.';
        document.getElementById('file-input').value = '';
        // setTimeout(() => {
        //     document.getElementById('file-error-mssg').innerHTML = ''
        // }, 1000)
    } else {
        document.getElementById('file-error-mssg').innerText = '';
    }
}
