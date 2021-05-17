
//turn on to make the photo follow mouse
// $(document).ready(function()
// {
//     $(document).mousemove(function( event ) 
//     {
//         var docWidth = $(document).width();
//         var docHeight = $(document).height();
//         var xValue = (event.clientX/docWidth)*100;
//         var yValue = (event.clientY/docHeight)*100;
//         $('.photo').css('background-position', xValue+'%,'+yValue+'%');
//     });
// });


// ────────────────────────────────────────────────────────────────────────────────


var popped = false

function dimBG() {

  if ( !!popped ) { randomGif() }

  document.documentElement.style.overflow = "hidden"
  document.body.style.overflow = "hidden"

  document.getElementById("profileModal").style.display = "unset"
  dimNode = document.createElement("div")
  dimNode.classList.add("dim");
  dimNode.setAttribute("id", "dimCover")
  dimNode.setAttribute("onmouseover", "revertempUnDim()")
  dimNode.setAttribute("onclick", "undimBG()")
  document.body.appendChild(dimNode);
}

var dimmed = false
function firstdim() { 
  if ( document.getElementById("profileModal").style.display != "none" ) {
    if ( dimmed == false ) { dimmed = true }
  }
}

function revertempUnDim() {
  if ( dimmed == true ) { document.getElementById("dimCover").style.opacity = .01 }
}

function undimBG() {
  dimmed = false
  document.getElementById("profileModal").style.display = "none"
  document.getElementById("dimCover").remove()
  if ( popped == false ) { popped = true }
}


// ────────────────────────────────────────────────────────────────────────────────


panels = [
    {
        "backgroundImage" : 'url("gifs/bw/flying-birds.webp"), url("gifs/bw/pixel-storm.webp")',
        "background-blend-mode" : "soft-light",
        "backgroundPosition" : "top right, center",
        "background-repeat" : "no-repeat, no-repeat",
        "backgroundSize" : "cover, 80% 65%",
        "filter" : "brightness(78%) grayscale(95%) saturate(30%)"
    },
    {
        "backgroundImage" : "url('pictures/wallpaperflare.com_wallpaper (3) (copy).jpg')",
        "backgroundSize" : "cover",
        "filter" : "none"

    },
    {
        "backgroundImage" : "url('pictures/bw3.jpg')",
        "backgroundSize" : "cover",
        "filter" : "none"

    },
    {
        "backgroundImage" : "url('pictures/wallpaperflare.com_wallpaper (4) (copy).jpg')",
        "backgroundSize" : "cover",
        "filter" : "none"

    },
    {
        "backgroundImage" : "url('pictures/wallpaperflare.com_wallpaper (3) (copy).jpg')",
        "backgroundSize" : "cover",
        "filter" : "none"
    },
    {
        "backgroundImage" : "url('pictures/wallpaperflare.com_wallpaper (6).jpg')",
        "backgroundSize" : "cover",
        "filter" : "none"
    },
    {
        "backgroundImage" : "url('pictures/1.jpg')",
        "backgroundSize" : "cover",
        "backgroundPosition" : "center",
        "filter" : "none"
    },
    {
        "backgroundImage" : "url('pictures/647786.jpg')",
        "backgroundSize" : "cover",
        "backgroundPosition" : "center",
        "filter" : "grayscale(85%) brightness(78%) opacity(100%) saturation(100%)"
    },
    {
        "backgroundImage" : "url('pictures/annalisa-bellini-sn-Qmo6CCIM-unsplash.jpg')",
        "backgroundSize" : "cover",
        "filter" : "grayscale(100%)"
    },
    {
        "backgroundImage" : "url('pictures/1313179.jpg')",
        "backgroundSize" : "cover",
        "filter" : "none",
        "backgroundPosition": "bottom"

    },
    {
        "backgroundImage" : 'url("gifs/film-noir/media1.giphy.com_media_Tk79kO0ELC7WpmR4xW_200w.webp")',
        "backgroundPosition" : "center",
        "backgroundSize" : "cover",
        "filter" : "brightness(78%) grayscale(95%)"
    },
    {
        "backgroundImage" : 'url("gifs/film-noir/audrey-fish.webp")',
        "backgroundPosition" : "top",
        "backgroundSize" : "cover",
        "filter" : "opacity(90%) grayscale(95%)"
    },    
    {
        "backgroundImage" : 'url("gifs/film-noir/media4.giphy.com_media_SvEeTSlDs7YBDqp7M4_200w.webp")',
        "backgroundPosition" : "center",
        "backgroundSize" : "cover",
        "filter" : "brightness(78%) grayscale(95%)"
    },    
    {
        "backgroundImage" : 'url("gifs/film-noir/media0.giphy.com_media_3gNpW2a8WK04N5Ybmv_200.webp")',
        "backgroundPosition" : "center",
        "backgroundSize" : "cover",
        "filter" : "brightness(78%) grayscale(95%)"
    },    
    {
        "backgroundImage" : 'url("gifs/bw/media4.giphy.com_media_l2QE5bDTfjOKHmme4_200w.webp")',
        "backgroundPosition" : "center",
        "backgroundSize" : "cover",
        "filter" : "brightness(78%) grayscale(95%)"
    },    
    {
        "backgroundImage" : 'url("gifs/bw/media2.giphy.com_media_LLYMoDblVhhjvjRBtj_200w.webp")',
        "backgroundPosition" : "center",
        "backgroundSize" : "cover",
    },
    {
        "backgroundImage" : 'url("gifs/bw/flying-birds.webp")',
        "backgroundPosition" : "center",
        "backgroundSize" : "cover",
        "filter" : "brightness(76%) grayscale(90%)"
    },
    {
        "backgroundImage" : 'url("gifs/pixel-art/pixel-art20.webp")',
        "backgroundPosition" : "center",
        "backgroundSize" : "cover",
        "filter" : "brightness(78%) grayscale(98%)"
    },
    {
        "backgroundImage" : 'url("gifs/pixel-art/pixel-art28.webp")',
        "backgroundPosition" : "center",
        "backgroundSize" : "cover",
        "filter" : "grayscale(100%)"
    },
    {
        "backgroundImage" : 'url("gifs/pixel-art/pixel-art39.webp")',
        "backgroundPosition" : "center",
        "backgroundSize" : "cover",
        "filter" : "grayscale(100%)"
    },
]

// Random Gif Panel Loader
function randomGif() {
    rindex = Math.floor( Math.random() * ( panels.length - 1 ) )
    newGif = panels[rindex]
    n = document.getElementsByClassName("banner")[0].style

    for ( const k of Object.keys(newGif) ) {
        console.log(k)
        console.log(n[k])
        console.log(newGif[k])
        n[k] = newGif[k]
    }
}