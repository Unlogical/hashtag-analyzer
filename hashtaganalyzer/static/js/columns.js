function showPosColumn() {
		pos_column = document.getElementById("pos_col")
		neu_column = document.getElementById("neu_col")
		neg_column = document.getElementById("neg_col")
		show(pos_column);
		hide(neu_column);
		hide(neg_column);
		wide(pos_button);
		small(neu_button);
		small(neg_button);
}

function showNeuColumn() {
		pos_column = document.getElementById("pos_col")
		neu_column = document.getElementById("neu_col")
		neg_column = document.getElementById("neg_col")
		hide(pos_column);
		show(neu_column);
		hide(neg_column);
		small(pos_button);
		wide(neu_button);
		small(neg_button);
}

function showNegColumn() {
		pos_column = document.getElementById("pos_col")
		neu_column = document.getElementById("neu_col")
		neg_column = document.getElementById("neg_col")
		hide(pos_column);
		hide(neu_column);
		show(neg_column);
		small(pos_button);
		small(neu_button);
		wide(neg_button);
}


function hide(column) {
	column.style.display = "none";
}
	
function show(column) {
	column.style.display = "block";
}

function wide(button) {
	button.classList.add('wide');
	button.classList.remove('small');
}

function small(button) {
	button.classList.add('small');
	button.classList.remove('wide');
}

function columns(){
		width=document.body.clientWidth;
		if (width >= 1000) {
			show(pos_column);
			show(neu_column);
			show(neg_column);
		}
}