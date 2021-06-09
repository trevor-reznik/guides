

//-------------Random Generators-------------\\

// -random rgba generator- \\
function random_rgba() {
  var o = Math.round, r = Math.random, s = 255;
  ranColor = 'rgba(' + o(r()*s) + ',' + o(r()*s) + ',' + o(r()*s) + ',' + r().toFixed(1) + ')';
}

function randomHex() {
  var letters = '0123456789ABCDEF';
  var color = '#';
  for (var i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}

function rColor(alphaValue) {
  alphaValue = alphaValue || (Math.random() * 1).toPrecision(2)
  return tinycolor.random().setAlpha(alphaValue).toRgbString() 
}

function randomReadable(bgColor) {
  colorIter = rColor(1)
  for (let i = 0; i < 100; i++) {
      if ( tinycolor.isReadable(colorIter, bgColor, {level: "AAA"}) == false ) {
          colorIter = rColor(1)
      } 
      else { return colorIter } 
  }
  return tinycolor.mostReadable(bgColor, ["FF09CE", "FFFFFF", "000000", "424343", "361D2E", "2BFFD1", "4FE5FF", "FF5A4B"]).toHexString()
}

function randomComplement(bgColor, partner) {
  colorIter = tinycolor(partner).complement().toString()
  for (let i = 0; i < 100; i++) {
      if ( tinycolor.isReadable(colorIter, bgColor, {level: "AAA"}) == false ) {
      // Spin 5 degrees on color wheel until complement is readable on bg color
      colorIter = tinycolor(colorIter).spin(5).toString()
      } 
      else { return colorIter }
  }
  return tinycolor.mostReadable(bgColor, ["FF09CE", "FFFFFF", "000000", "424343", "361D2E", "2BFFD1", "4FE5FF", "FF5A4B"]).toHexString()
}

//-------------Color Model Convertors-------------\\


// -rgb to hex- \\
function componentToHex(c) {
  var hex = c.toString(16);
  return hex.length == 1 ? "0" + hex : hex;
}
function rgbToHex(r, g, b) {
  return "#" + componentToHex(r) + componentToHex(g) + componentToHex(b);
}

//-------------Inversion & Contrast-------------\\


// -rgb inverter -- contrast generator- \\
function invert(rgb) {
  rgb = [].slice.call(arguments).join(",").replace(/rgb\(|\)|rgba\(|\)|\s/gi, '').split(',');
  for (var i = 0; i < rgb.length; i++) rgb[i] = (i === 3 ? 1 : 255) - rgb[i];
  return rgb
}

//background contrasting rgba generator
function rgbaContrast(rgb) {
      var colors = {};
      // check if we are receiving an element or element background-color
      if (rgb instanceof jQuery) {
          rgb = rgb.css('background-color');
      }
      rgb = rgb.split(/\(([^)]+)\)/)[1].replace(/ /g, '');
      var r = parseInt(rgb.split(',')[0], 10),
          g = parseInt(rgb.split(',')[1], 10),
          b = parseInt(rgb.split(',')[2], 10),
          a;
      // if RGBA, map alpha to variable (not currently in use)
      if (rgb.split(',')[3] !== null) {
          a = parseInt(rgb.split(',')[3], 10);
      }
      // standard grayscale algorithmic formula
      var contrast = (Math.round(r * 299) + Math.round(g * 587) + Math.round(b * 114)) / 1000;
      return contrast;
};


function contrastGenhex(hex){
	/* http://www.webmasterworld.com/r.cgi?f=88&d=9769&url=http://www.w3.org/TR/AERT#color-contrast
	Color brightness is determined by the following formula: 
	((Red value X 299) + (Green value X 587) + (Blue value X 114)) / 1000 */
	threshold = 130; /* about half of 256. Lower threshold equals more dark text on dark background  */			
	function cutHex(h) {return (h.charAt(0)=="#") ? h.substring(1,7):h};
	hRed = parseInt((cutHex(hex)).substring(0,2),16);
	hGreen = parseInt((cutHex(hex)).substring(2,4),16);
	hBlue = parseInt((cutHex(hex)).substring(4,6),16);			      
	cBrightness = ((hRed * 299) + (hGreen * 587) + (hBlue * 114)) / 1000;
	 // if (cBrightness > threshold){return "#000000";} else { return "#ffffff";}	
	//test colortable
	var theColor;
	var textcolor;
	var colPairs = new Array("00","22","44","66","99","aa","cc","ff");
	for(i=0;i<colPairs.length;i++){
		for(j=0;j<colPairs.length;j++){
			for(k=0;k<colPairs.length;k++){
				theColor = "#"+colPairs[i]+colPairs[j]+colPairs[k];
				textcolor = contrastGenhex(theColor);	
				alert(theColor)
				alert(textcolor)		
			}
	}
}
}


//-------------Complementary & Matching-------------\\

function complementaryHex(colorInput) {
	return 0xffffff ^ colorInput
}


