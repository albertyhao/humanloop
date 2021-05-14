const ruleTemplate = document.querySelector("#ruleTemplate");
const inputFunction = document.querySelector("#inputFunction");
const ruleType = document.querySelector("#ruleType");
const addRule = document.querySelector("#addRule");
const cancelRule = document.querySelector("#cancelRule");
const cancelPythonFunction = document.querySelector("#cancelPythonFunction");
const addPythonFunction = document.querySelector("#addPythonFunction");
const savePythonCode = document.querySelector("#saveCode");
const testPythonCode = document.querySelector("#testCode");


const inputPythonbtn = document.querySelector("#inputPythonbtn");
const inputPython = document.querySelector("#inputPython");

//rule template event listeners
ruleTemplate.addEventListener("click", () => {
	ruleType.style.display = "block";
})

addRule.addEventListener("click", () => {
	ruleType.style.display = "none";
})

cancelRule.addEventListener("click", () => {
	ruleType.style.display = "none";
})

//python function event listeners
addPythonFunction.addEventListener("click", () => {
	inputPython.style.display = "none";
})

cancelPythonFunction.addEventListener("click", () => {
	inputPython.style.display = "none";
})

inputPythonbtn.addEventListener("click", () => {
	inputPython.style.display = "block";
	console.log("works");
})

testPythonCode.addEventListener("click", () => {
	grabPython();
})

savePythonCode.addEventListener("click", () => {
	window.saveContents();
})

// grab user code from qoom editor

async function grabPython(){
	const output = document.querySelector('#output');
	var c = editor.getValue();

	var data = {code: c};
	var res = await fetch('/humanloop/python', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify(data)
	})

	var text = await res.text();
	output.value = text;
	console.log(text);

	//output.innerText = code;
	//console.log("qoom code: \n", code);
}
