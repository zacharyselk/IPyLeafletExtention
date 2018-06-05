HTML_BUTTON = '''<html>
<div>
<p id='station_name'>%s</p>
<p id='lat'>Latitude: %s<br>Longitude: %s</p>
<p id='index' hidden>%s</p>

<button type='button' onclick='var var_station = document.getElementById("station_name").innerHTML; 
var var_index = document.getElementById("index").innerHTML; 
var command = "SET_GLOBAL_SHOW_STATION(" + var_index + ")"; 
console.log("Executing Command: " + command); 
var kernel = IPython.notebook.kernel; kernel.execute(command); 
comm = Jupyter.notebook.kernel.comm_manager.new_comm("_button_");
comm.send({"hello": "goodbye"});'>Show in table</button>
</div>
</html>'''
