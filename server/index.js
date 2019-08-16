const express = require('express');
const app = express();
const port = 3000;

app.post("/reservation", (req, res) => {
 res.send("Welcome to a basic express App");
});

app.listen(port, () => {
  console.log(`Example app listening on port ${port}!`)
});


// var nodemailer = require('nodemailer');
//
// var transporter = nodemailer.createTransport({
//   service: 'gmail',
//   auth: {
//     user: 'gaziellosl@gmail.com',
//     pass: 'PSS'
//   }
// });
//
// var mailOptions = {
//   from: 'gaziellosl@gmail.com',
//   to: 'gaziellosl@gmail.com',
//   subject: '',
//   text: ''
// };

// app.use(bodyParser.json()) // for parsing application/json
// app.use(
//   bodyParser.urlencoded({
//     extended: true
//   })
// ) // for parsing application/x-www-form-urlencoded

//This is the route the API will call
// app.post('/new_message', function(req, res) {
//   console.log("Received new booking")
//   const { message } = req.body
//
//   console.log(message)
//   return;
//
//   mailOptions.subject = message;
//   mailOptions.text = message;
//
//   transporter.sendMail(mailOptions, function(error, info){
//     if (error) {
//       console.log(error);
//     } else {
//       console.log('Email sent: ' + info.response);
//     }
//   });
// })
//
// // Finally, start our server
// app.listen(3000, function() {
//   console.log('Listening for reserves in www.lacasaazullanzarote.com !')
// })
