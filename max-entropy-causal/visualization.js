// Note: P5 js library required (ran on Open Processing)
let table;
// local array to store values
let VALUES = [];
const PADDING = 60;
// 391 iterations, 100 columns - 1 per each cluster
let ROWS = 391;
let COLUMNS = 100;
const CELL_SIZE = 65;
let MAX_COLOR_VAL = Number.MIN_VALUE;
// load file
function preload(){
	table = loadTable("all_grads.csv", "csv");
}


function processCSV(){
	for(let i = 0; i < ROWS; i++) {
		VALUES.push(new Array(COLUMNS));
	}
	ind = 0
	
	for (let r = 0; r < table.getRowCount(); r++){
		let currentRow = table.getRow(r);
		for (var i = 0; i < currentRow["arr"].length; i++) { 
			VALUES[ind][i] = parseFloat(currentRow["arr"][i]);
		}
		ind +=1;
	}
	
}

// for debugging and visibility
function printValues(){
	for (let i = 0; i<ROWS;i++){
		for (let j = 0; j< COLUMNS;j ++){
			print(VALUES[i][j]);
		}
	}
}

// actual rendering function
function setup() {
	createCanvas(windowWidth, windowHeight);
	// print(table.getRowCount() + ' total rows in table');
	// print(table.getColumnCount() + ' total columns in table');
	ind = 0;
	for(let i = 0; i < ROWS; i++) {
		VALUES.push(new Array(COLUMNS));
	}
	// load values
	for (let r = 0; r < table.getRowCount(); r++){
		let currentRow = table.getRow(r);
		for (var i = 0; i < currentRow["arr"].length; i++) { 
			VALUES[ind][i] = parseFloat(currentRow["arr"][i]);
			if (VALUES[ind][i] > MAX_COLOR_VAL){
				MAX_COLOR_VAL = VALUES[ind][i];
			}
		}
		ind +=1;
	}

}

// global pointer
let ptr = 0;
function label(){
	return "Iteration #: " + ptr.toString();
}

// rendering
// draw function
function draw(){
	// print(FREQ);
	background("#ced1e0");

	translate(windowWidth/4,0);
	noStroke();

	// initialize colors
  let from = color(242, 193, 107); // yellow (lower values)
  let to = color(114, 102, 150); // purple (higher values)
	
	// just do the 10th batch of 100
	for (let i = 0; i < 10; i++){
		for (let j = 0; j < 10; j++){

			colInd = i * 10 + j
			let left = PADDING + (j*CELL_SIZE);
			let top = PADDING + (i*CELL_SIZE);
			let sz = CELL_SIZE - 2;
			// global maximum did not produce any significant visual findings
			// trying: relative maximum within each row of 10 values (not surw how accurate this would be)
			this_max_value = Math.max(...VALUES[ptr]);
			var c = lerpColor(from, to, (VALUES[ptr][colInd]/ this_max_value));
			// fill in heatmap square
			fill(c)
			rect(left,top,sz,sz);
			
			// text labeling
			fill('#382b54');
			textSize(13); 
			text(colInd+1, left+10, top+20);

			if (i == 0 && j == 0){
				textSize(30); 
				fill('#382b54');
				text("(Gradient) Epoch Iteration #: " + ptr, left, top-10);
			}
		}
	}
	
  if (frameCount % 60 == 0 && ptr+15 < 391) {
    ptr +=15;
  }
}

