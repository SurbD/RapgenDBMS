function closeAlert() {
    flash_card = document.getElementById("flash-alert-id");

    if (flash_card === "none" ) {
        flash_card.style.display = "block"
    } else {
        flash_card.classList.add("close-animation")
        setTimeout(() => {
            
            flash_card.style.display = "none"
            flash-card.classList.remove("close-animation")
        }, 600)
    }
}


