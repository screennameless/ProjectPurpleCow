//Closure to copy "html_id" into the click callback
function clickCallback(html_id, callback) {
    return function() {
        return callback(html_id);
    }
}

//Register the button to respond to click events
function register_button(button_id, callback) {
    html_id = "#" + button_id; //Generate HTML element ID name

    //Register click callback
    $(html_id).click(clickCallback((' ' + html_id).slice(1), function(html_id) { //Force a deep-copy of the string into the callback
        if(!$(html_id).hasClass("disabled")) { //Button is not already disabled, so we can act on the click event
            $(html_id).addClass("disabled"); //Disable the button until event is complete
            $.get("/hit/" + button_id, function(response) { //Hit the API
                callback(response); //Call custom callback defined in HTML file
                $(html_id).removeClass("disabled"); //Re-enable the button
            })
        }
    }));
}
