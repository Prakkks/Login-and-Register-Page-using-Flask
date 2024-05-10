// const loginform = document.getElementById('form-controls')

// loginform.addEventListener('submit',async function(event)
// {
//     console.log("js started");
//     event.preventDefault();
//     const formData = new FormData(this);
//             // const username = formData.get('username');
//             const password = formData.get('password');
//             const email = formData.get('email');

//             try {
//                 const response = await fetch('/login', {
//                     method: 'POST',
//                     headers: {
//                         'Content-Type': 'application/json'
//                     },
//                     body: JSON.stringify({ email, password })
//                 });
//                 const data = await response.json();
//                 if (response.ok) {
//                     document.getElementById('message').innerText = data.message;
//                 } else {
//                     throw new Error(data.message);
//                 }
//             } catch (error) {
//                 document.getElementById('message').innerText = 'Error: ' + error.message;
//             }
// });


