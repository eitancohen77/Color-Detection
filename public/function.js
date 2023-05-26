const canvas = document.getElementById('canvas1')
const ctx = canvas.getContext('2d')
const image1 = new Image();
let color_name = document.getElementById('colorName')
let color = document.getElementById('color')
image1.src = 'photo.avif'
image1.classList.add('imageClass')
canvas.width = 800;
canvas.height = 450;

image1.addEventListener('load', function() {
    ctx.drawImage(image1, 0, 0, 800, 450)
})

// What we do here is we create a canvas and we frame the image onto that canvas
// Reason why is because we can then use the getImageData function which allows 
// us to map the image onto a 2D picture where we can manipulate pixels.
// Here we use it to get the RGB of any pixel in the image(canvas).
/* canvas.addEventListener('load', function() {
    ctx.drawImage(canvas, 0, 0)
}) */

canvas.addEventListener('click', function(event) {
    const x = event.offsetX;
    const y = event.offsetY;

    const pixelData = ctx.getImageData(x, y, 1, 1).data;
    const red = pixelData[0];
    const green = pixelData[1];
    const blue = pixelData[2];

    const rgb = (`rgb(${red}, ${green}, ${blue})`);
    input = {'rgb': rgb}

    process_data(input).then((returnedData) => {
        color_name.textContent = returnedData['color_name']
        color_name.style.color = `rgb(${returnedData['red']}, ${returnedData['green']}, ${returnedData['blue']})`
        color.style.backgroundColor = `rgb(${returnedData['red']}, ${returnedData['green']}, ${returnedData['blue']})`

    })

    /* fetch('/handle_rgb', {
        method: 'POST',
        body: JSON.stringify({'rgb': rgb}),
        headers: {'Content-Type': 'application/json'}
    })
    .then(response => response.json())
    .then(data => {
        console.log('Data received from server:', data);
        color_name.textContent = data['color_name']
        console.log(data['red'])

    })
    .catch(error => {
        console.error('Error:', error);
    }); */
});

async function process_data(data) {
    try {
        const response = await fetch('/process-data', {
            method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
        });
        const result = await response.json();
        console.log(result);

        return result;
    } catch(error) {
        console.log('Error:', error);
        return null
    }
}