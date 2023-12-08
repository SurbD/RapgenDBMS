const form = document.forms["database-upload-form"];
const email = form["email"];
const dateOfBirth = form["dateOfBirth"];
const phoneNumber = form["phoneNumber"];
const lastName = form["lastName"];
const firstName = form["firstName"];
const role = form["role"];
const region = form["region"];
const gender = form["gender"];

const emailRegExp =
  /^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$/;
const nameRegExp = /^([a-zA-Z])([a-zA-Z])/;
const numberRegExp = /^[789]\d+$/;

// Setting Valid variables
let emailValid = true;
let firstNameValid;
let lastNameValid;
let dateOfBirthValid;
let phoneNumberValid;

let emailValue;
let validEmail = null;

function formToDatabase() {
  if (email.value === "" || email.value == false) {
    emailValue = null;
  } else {
    emailValue = email.value.toLowerCase();
  }

  const formData = {
    first_name: firstName.value.toLowerCase(),
    last_name: lastName.value.toLowerCase(),
    email: emailValue,
    gender: gender.value,
    date_of_birth: dateOfBirth.value,
    phone_number: `+234${phoneNumber.value}`,
    role: role.value,
    region: region.value,
  };

  const promise = axios.post("/upload-form", formData);
  const resPromise = promise.then((response) => response.data);

  return resPromise;
}

// This determines what happens when a user tries to submit th form
form.addEventListener("submit", () => {
  event.preventDefault();

  // const formValid = null; // call function that will check form validity
  if (checkFormValid()) {
    console.log("Form is valid you can now submit.");
    formToDatabase()
      .then((data) => {
        const responds = data.status;
        console.log(`From formToDatabase function --> status:${responds}`);
      })
      .catch((err) => console.log(err));
  } else {
    console.log("Invalid Form inputs please check for and try again");
  }
});

email.addEventListener("input", () => {
  const isValid = email.value.length == 0 || emailRegExp.test(email.value);

  if (isValid) {
    console.log("Valid email format");
    if (email.value.length != 0) {
      emailValidator()
        .then((data) => {
          validEmail = data.exists;
          console.log("Email Valid");
        })
        .catch((err) => console.log(err));
    }
    emailValid = true;
    email.classList.remove("invalid-file-form");
  } else {
    email.classList.add("invalid-file-form");
    console.log("Invalid email format");
    emailValid = false;
  }
});

dateOfBirth.addEventListener("input", () => {
  // Checks if year is less then or is equal to current year
  console.log(dateOfBirth.value);
});

phoneNumber.addEventListener("input", () => {
  const isValid =
    phoneNumber.value.length == 0 ||
    (numberRegExp.test(phoneNumber.value) && phoneNumber.value.length == 10);
  // Checks if phone number matches any of the formats given

  if (isValid) {
    phoneNumberValid = true;
    phoneNumber.classList.remove("invalid-file-form");
    console.log(`PhoneNumber '${phoneNumber.value}' - ${isValid}`);
  } else {
    phoneNumberValid = false;
    phoneNumber.classList.add("invalid-file-form");
  }
});

firstName.addEventListener("input", () => {
  const isValid =
    firstName.value.length == 0 ||
    (nameRegExp.test(firstName.value) && firstName.value.length >= 3);

  if (isValid) {
    firstNameValid = true;
    firstName.classList.remove("invalid-file-form");
  } else {
    firstNameValid = false;
    firstName.classList.add("invalid-file-form");
  }
});

lastName.addEventListener("input", () => {
  const isValid =
    lastName.value.length == 0 ||
    (nameRegExp.test(lastName.value) && lastName.value.length >= 3);

  if (isValid) {
    lastNameValid = true;
    lastName.classList.remove("invalid-file-form");
  } else {
    lastName.classList.add("invalid-file-form");
    lastNameValid = false;
  }
});

function emailValidator() {
  const data = {
    first_name: firstName.value,
    email: email.value,
  };
  const promise = axios.post("/validate-email", data);
  const dataPromise = promise.then((response) => response.data);
  console.log("sending email valid");

  return dataPromise;
}

function checkFormValid() {
  const formValid =
    emailValid && lastNameValid && firstNameValid && phoneNumberValid; // others later added
  // let validEmail = null;
  let isValid = false;
  console.log("in form valid checker");

  // if (email.value.length != 0) {
  //   emailValidator()
  //     .then((data) => {
  //       validEmail = data.exists;
  //       console.log(validEmail);
  //       console.log("Email Valid");
  //     })
  //     .catch((err) => console.log(err));
  // }

  if (formValid && (validEmail == null || validEmail == false)) {
    isValid = true;
  }

  return isValid;
}
