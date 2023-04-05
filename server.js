const express = require('express');
const app = express();
const path = require('path');
const ejsMate = require('ejs-mate')
app.engine('ejs', ejsMate);
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');
app.use(express.static(path.join(__dirname, 'public')))
const { spawn } = require('child_process');
// bodyParser is needed in order to send data from client to server
const bodyParser = require('body-parser');

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));


app.get('/', (req, res) => {
    res.render('index')
})

app.post('/process-data', (req, res) => {
    const input_data = req.body.rgb;
    console.log('The data from server ')
    console.log(input_data)
    // Here we are telling it to send the json data to transfer.py, 
    const pythonProcess = spawn('python3.11', ['./data.py', JSON.stringify(input_data)]);

    pythonProcess.stdout.on('data', output => {
      // Send the manipulated data back to the client
        console.log('Python script output:', output.toString());
        res.json(JSON.parse(output));
    });

    pythonProcess.stderr.on('data', error => {
        // Handle errors
        console.error('Python script error:', error.toString());
        res.status(500).send('An error occurred while processing the data.');
    });
});

app.listen(3000, () => {
    console.log('Serving on Port 3000')
})