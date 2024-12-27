import { app } from "../../../scripts/app.js";
import { ComfyWidgets } from "../../../scripts/widgets.js";

// Displays input text on a node

app.registerExtension({
	name: "io.SimpleStringRepository",
	async beforeRegisterNodeDef(nodeType, nodeData, app) {
		if(nodeType?.comfyClass.startsWith('SimpleStringRepository')){
			//TODO Perhaps add stuff
		}
	},
	async nodeCreated(node, app) {
		let nodeClass= node?.comfyClass;
		if(nodeClass.startsWith('SimpleStringRepository')){
			let isCompact = node?.comfyClass.endsWith('Compact');

			let extractParsedStrings = ()=>{
				let str_widget = node.widgets[0];
				let str = str_widget.value;
				return str.split('\n');
			}

			//Adds numerical indexes to strings, does not destroy or change existing ones.
			node.addWidget("button", "✍ Add Missing Indexes", null, () => {
				let currentStrings = extractParsedStrings();
				let map = {}
				let orphans = {};
				for(let i in currentStrings){
					let index = null;
					let str = currentStrings[i];
					if(str.includes('.')){
						index = str.split('.')[0];
						str = str.split('.')[1];
					}
					if(!index || map[index])
						orphans[i] = str;
					else 
						map[index] = str;
				}
				let newIndex = 1;
				for(let i in orphans){
					while(map[newIndex] !== undefined)
						newIndex++;
					currentStrings[i] = newIndex + '.' + orphans[i];
					map[newIndex] = orphans[i];
				}
				node.widgets[0].value = currentStrings.join('\n');
			}, { serialize: false });

			//Regenerates all string indexes, potentially changing existing ones.
			node.addWidget("button", "⚠ Regenerate All Indexes", null, () => {
				let currentStrings = extractParsedStrings();
				for(let i in currentStrings){
					if(currentStrings[i].includes('.'))
						currentStrings[i] = currentStrings[i].split('.')[1];
					currentStrings[i] = (i-0+1) +'.'+ currentStrings[i];
				}
				node.widgets[0].value = currentStrings.join('\n');
			}, { serialize: false });

			//Strips all strings of their indexes
			node.addWidget("button", "❌ Remove All Indexes", null, () => {
				let currentStrings = extractParsedStrings();
				for(let i in currentStrings){
					if(currentStrings[i].includes('.'))
						currentStrings[i] = currentStrings[i].split('.')[1];
				}
				node.widgets[0].value = currentStrings.join('\n');
			}, { serialize: false });

			//Resets Parameters (Target/Strength/Randomness)
			node.addWidget("button", "↺ Reset Target Parameters", null, () => {
				for(let i in node.widgets){
					let widget = node.widgets[i];
					switch(isCompact){
						case true:
							if(widget.name.match(/^target\d+$/))
								widget.value = '0,1,-1';
							break;
						case false: 
							if(widget.name.match(/^target\d+$/))
								widget.value = 0;
							if(widget.name.match(/^strength\d+$/))
								widget.value = 1;
							if(widget.name.match(/^random\d+$/))
								widget.value = -1;
							break;
					}
				}
			}, { serialize: false });
		}
	},
});
