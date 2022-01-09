testing = () =>{
    alert("Working");
}

names = ['calendar', 'music', 'alarms', 'weather'];

hideWindow = (name) => {
    windowName = document.getElementById('pop-up-window-' + name);
    windowName.style.display = 'none';
};

showWindow = (name) => {
    windowName = document.getElementById('pop-up-window-' + name);
    windowName.style.display = 'block';
    for(var i in names){
        if(names[i] != name){
            hideWindow(names[i]);
        }
    }
};