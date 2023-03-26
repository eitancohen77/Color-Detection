const canvas = document.getElementById('canvas1')
const ctx = canvas.getContext('2d')
canvas.width = 800;
canvas.height = 450;

const image1 = new Image();
image1.src = "/public/photo.avif"

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