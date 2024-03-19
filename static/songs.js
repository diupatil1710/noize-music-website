console.log("welcome to music");
// Initialize the variable
let songIndex = 0;
let audioElement = new Audio("./songs/desi girl.mp3");
let masterPlay = document.getElementById('masterPlay');
let progressbar=document.getElementById('myProgressBar');
let gif= document.getElementById('gif');
let songItem = Array.from( document.getElementsByClassName("songItem"));


let songs=[
    {songName:"Desi girl",filePath:'songs/desi girl.mp3',coverPath:"music/e1.jpg"},
    {songName:"log kehate pagal",filePath:'songs/log kehate pagal.mp3',coverPath:"music/e2.jpg"},
    {songName:"man mandir me saje bhihari",filePath:'songs/man mandir me saje bhihari.mp3',coverPath:"music/e3.jpg"},
    {songName:"shivji teri lila nyari",filePath:'songs/shivji teri lila nyari.mp3',coverPath:"./music/e4.jpg"},
    {songName:"mere ghar ram aaye hain",filePath:'songs/man mandir me saje bhihari.mp3',coverPath:"music/e5.jpg"},
    {songName:"mere ghar ram aaye hain",filePath:'songs/man mandir me saje bhihari.mp3',coverPath:"music/e6.jpg"},
    {songName:"mere ghar ram aaye hain",filePath:'songs/man mandir me saje bhihari.mp3',coverPath:"music/e7.jpeg"},
    // {songName:"mere ghar ram aaye hain",filePath:'songs/man mandir me saje bhihari.mp3',coverPath:"music/a.jpg"},

]

// songItem.forEach((element,i)=>{
    // console.log(element,i);
    // element.getElementsByTagName("img")[0].src = songs[i].coverPath;
    // element.getElementsByClassName("songName")[0].innerText = songs[i].songName;
// })
masterPlay.addEventListener('click',()=>{
    if(audioElement.paused || audioElement.currentTime<=0){
        audioElement.play();
        gif.style.opacity = 1;
        document.getElementById("masterPlay").src="pause-solid.svg"
        
    }
    else{
        audioElement.pause();
        gif.style.opacity = 0;
        document.getElementById("masterPlay").src="play-solid.svg"
    }
})
// listen to Event
audioElement.addEventListener('timeupdate',()=>{
    // seek bar update
    progress = parseInt((audioElement.currentTime/audioElement.duration)*100);
    progressbar.value = progress;
})
progressbar.addEventListener('change',()=>{
    audioElement.currentTime = progressbar.value * audioElement.duration/100;

})


// const makeAllPlay= ()=>{
//     Array.from(document.getElementsByClassName("songItemPlay")).forEach((element)=>{
        
//     })
// }

Array.from(document.getElementsByClassName("songItemPlay")).forEach((element)=>{
    element.addEventListener('click',(e)=>{
        console.log(e.target.id);
        index = e.target.id;
        // e.target.classList.remove("")
        audioElement.src = `songs/${index}.mp3`;
        audioElement.currentTime = 0;
        audioElement.play();
        // e.getElementsByClassName("songName")[0].innerText = songs[i].songName;
        
    })

})