console.log('Preparing to simplify');

var elements = document.getElementsByTagName("*"); for (var x = 0; x < elements.length; x++) {
  	var anelement = elements[x];

  	for (var y = 0; y < anelement.childNodes.length; y++) {
  		var node = anelement.childNodes[y];
  		if (node.nodeType == 3) {
  			var text = node.nodeValue
  			if (/\S/.test(text) && node.parentNode.tagName != "SCRIPT" && node.parentNode.tagName != "STYLE") {
          console.log(node.parentNode.tagName)
          
  				//var res = text.split(" ")
  				//for (var z = 0; z < res.length; z++) {
  				//	if (/\S/.test(res[z])) {
  						//console.log("Bleh:" + res[z] + ":");
  				//		var temptext = res[z];
  				//text = text.replace(/[.,\/#!$%\^&\*;:{}=_`~()]/g,"")
          text = text.replace(/\n/g, ' ');
          if (text.slice(-1) == ' '){
              text += "%20";
          }
          console.log(text);
          var xmlHttp = new XMLHttpRequest();
          xmlHttp.open( "GET", "http://localhost:8000/"+text, false ); // false for synchronous request
          xmlHttp.send();
          var tempreplace = xmlHttp.responseText;
  				text = text.replace(text, tempreplace);
  				//	}
  				//}
  				anelement.replaceChild(document.createTextNode(text), node);
  			}
  		}

  	}
}

console.log('Done simplifying');
