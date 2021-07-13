//
// ─── READ THESE INSTRUCTIONS FIRST ──────────────────────────────────────────────
//

/**
 * Hit Ctrl+Shift+I to open the DevTools in Chrome
 *
 * On the top of the page in the 'Console' tab,
 * next to the clear console button,
 * there is a button that says 'top' which, when clicked,  will
 * display a list of available frames.
 *
 * Select the item in that list that includes the
 * phrase "api.playposit.com"
 *
 * Now Copy the stuff between this and the next section and then
 * paste it into the console and press Enter.
 *
 */

//
// ─── COPY AND PASTE THE BELOW INTO CONSOLE ───────────────────────────────────────
//

class PositFrame { constructor() {this.instructions();}
  instructions = () => {const steps=["Step 1.\nGo to the Network tab -> In the filter area, Click the 'XHR' filter -> \n\nBefore the next part: these instructions will dissapear after you do this, but you're going to reload the page and then paste the code into the console again after the reload finishes. Okay now reload (Ctrl+R)","Step 2.\nClick the first request in the 'Name' column (should start with 'bulb?bulb_id')","Step 3.\nClick 'Response' tab","Step 4.\nClick the text that it shows you (should be json data that starts with '{bulb:')","Step 5.\nCopy that test into clipboard (Ctrl+A -> Ctrl+C)","Step 6.\nGo to 'Console' tab again and type\nx.answer(``)\nbut paste your clipboard contents between the backticks in parentheses (!important: they are backticks not single quotes)\nThen press enter after you;ve pasted that shit in between the backticks. Answers should appear in top right of screen","Step 7.\nGo back tot the drop-down menu from ealier and now select the item that includes the phrase 'youtube.com' -- but it shouldn't be the very last item in the list -- it should be nested under the one you clicked before","Step 8.\nProceed to the next section in the script file where you started. and Copy and paste the next chunk of code into the console to finish.",];for (const step of steps) {console.log(step);}}; answer = (x) => {let answers = [];for (const choice of x.split("interactionOptions")) {if (choice && choice.includes("feedback")) {let properties = choice.split(":");for (const [index, word] of properties.entries()) {if (word && word.length > 0 && word.includes("correct")) {if (properties[index + 1].includes("1")) {answers.push(word);;}}}}}const answersOnly = [];answers.forEach((str) => answersOnly.push(str.split(",")[0].trim().replace(/\'|\"/g, "")));const div = document.createElement("div");div.setAttribute("style", "padding: 5px 10px; position: absolute; top: 0; right: 0; width: 15vw; height: auto; opacity: .7; z-index: 909; display: flex; flex-direction: column; justify-content: flex-start; overflow: visible;"); div.setAttribute("id", "customcustomcustom"); const css1 = document.createElement("style"); css1.innerHTML = `#customcustomcustom p { border: 3px solid skyblue; padding: 3px; box-sizing: border-box; background: white; margin: 5px; } #customcustomcustom p::before { content: "Correct Answer:"; margin-right: 1ch; color: blue; font-weight: 600;  } #customcustomcustom::after { content: "hide/show"; cursor: pointer; text-align: center; box-sizing: border-box; }`;div.innerHTML = answersOnly.join("");document.body.appendChild(div);document.querySelector("head").appendChild(css1); document.querySelector("#customcustomcustom").addEventListener("click", function () { this.style.opacity = this.style.opacity == 0.2 ? 1 : 0.2; });}; raiseControls = () => { const c = document.createElement("style"); c.innerHTML = `video::-webkit-media-controls.sizing-small div[pseudo="-internal-media-controls-button-panel" i] { align-items: baseline; z-index: 999; overflow: visible; } video::-webkit-media-controls-panel { justify-content: flex-start;height: 20%; }`; document.querySelector("head").appendChild(c); }; }; const x=new PositFrame();

// ────────────────────────────────────────────────────────────────────────────────
// ────────────────────────────────────────────────────────────────────────────────
// ────────────────────────────────────────────────────────────────────────────────
// ────────────────────────────────────────────────────────────────────────────────
// ────────────────────────────────────────────────────────────────────────────────
// ────────────────────────────────────────────────────────────────────────────────
// ────────────────────────────────────────────────────────────────────────────────
// ────────────────────────────────────────────────────────────────────────────────
// ────────────────────────────────────────────────────────────────────────────────
// ────────────────────────────────────────────────────────────────────────────────
// ────────────────────────────────────────────────────────────────────────────────
// ────────────────────────────────────────────────────────────────────────────────
// ─── DONT PROCEED TO THIS NEXT PART UNTIL YOU HAVE FINISHED THE INSTRUCTIONS IN
// ─── THE CONSOLE AND ARE PROMPTED ───────────────────────────────────────────────
//
//
//
// ─────────────────────────────────────────────────────────────────── PART 2 ─────
//

//
// ─── COPY AND PASTE THIS INTO THE CONSOLE ───────────────────────────────────────
//

class YTFrame {constructor(){this.ytv=document.querySelector("video");this.src=this.ytv.baseURI.trim().trim("blob:").trim('"').replace("embed","watch")+"&autoplay=true";this.url={full:this.src,base:this.src.split("?")[0],};this.a=document.createElement("a");this.a.setAttribute("target","_blank");console.log("\n\n\n-----------------------INSTRUCTIONS-------------------------:\n\nTo change to three times speed: x.speed(3)\nTo change to 5 times speed: x.speed(5)\netc. etc.\n\nTo open the source video at the current time (without being restricted from skipping): x.source()\n\nTo show the YT player controls: x.controls()\n\nTo change volume: x.volume(a number)\nTo get current time: x.time()\n\n\nYou can do something like entering: x.speed(10) and then just use the answer guide in the top right or (if the answer guide didn't work), enter: x.source() everytime an answer bulb prompts.\nThis allows you to do an hour long video quiz in less than 5 minutes.")}
time=()=>{return this.ytv.currentTime};speed=(x)=>{this.ytv.pause();this.ytv.playbackRate=x;this.ytv.play()};controls=()=>{this.ytv.controls=!0};volume=(x)=>{this.ytv.volume=x};source=()=>{let get=`${this.url.base}?t=${this.time()}`;this.a.setAttribute("href",get);this.a.click()} } const x = new YTFrame();