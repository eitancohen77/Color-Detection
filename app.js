// npm i express ejs ejs-mate body-parser
const express = require('express')
const app = express();
const path = require('path');
const ejsMate = require('ejs-mate')
// FOR THIS YOU WILL NEED THESE MODULE:
const { spawn } = require('child_process')
const bodyParser = require('body-parser');

app.engine('ejs', ejsMate);
app.set('view engine', 'ejs');
app.use(express.static(path.join(__dirname, 'public')))
app.set('views', path.join(__dirname, 'views'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));


app.get('/', (req, res) => {
    res.render('index.ejs')
})

app.post('/process-data', (req, res) => {
    const input = req.body;
    console.log(input)
    
    const pythonProcess = spawn('python', ['./KNN.py', JSON.stringify({'dataIn': input})]);
    let errorData = false, outputData = false;
    
    pythonProcess.stdout.on('data', output => {
        console.log('Python script output:', output);
        outputData = JSON.parse(output);
        if (errorData) {
            return res.status(500).send('An error occurred while processing the data.');
        }
        return res.json(outputData);
    });

    pythonProcess.stderr.on('data', error => {
        console.error('Python script error:', error.toString());
        errorData = true;
        if (outputData) {
            return res.status(500).send('An error occurred while processing the data.');
        }
    });
});

app.listen(3000, () => {
    console.log('Serving on Port 3000')
})