const canvas = document.getElementById('canvas1')
const ctx = canvas.getContext('2d')
canvas.width = 800;
canvas.height = 450;

const image1 = new Image();
image1.src = "/public/photo.avif"

// What we do here is we create a canvas and we frame the image onto that canvas
// Reason why is because we can then use the getImageData function which allows 
// us to map the image onto a 2D picture where we can manipulate pixels.
// Here we use it to get the RGB of any pixel in the image(canvas).
image1.addEventListener('load', function() {
    ctx.drawImage(image1, 0, 0)
})

canvas.addEventListener('click', function(event) {
    const x = event.offsetX;
    const y = event.offsetY;

    const imageData = ctx.getImageData(x, y, 1, 1);
    const pixelData = imageData.data;
    const red = pixelData[0];
    const green = pixelData[1];
    const blue = pixelData[2];

    console.log(`RGB(${red}, ${green}, ${blue})`);
});