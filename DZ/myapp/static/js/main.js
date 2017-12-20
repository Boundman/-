$('#add_review').on('submit', function (event) {
    event.preventDefault();
    console.log("form submitted!");  // sanity check
    create_review();
});

function create_review() {
    console.log("create review is working!"); // sanity check
    $.ajax({
        url: "add_review/", // the endpoint
        type: "POST", // http method
        data: {
            title: $('#title').val(), description: $('#description').val(),
            film_url: document.getElementById('film_name').innerHTML
        }, // data sent with the post request

        // handle a successful response
        success: function (json) {
            $('#title').val(''); // remove the value from the input
            $('#description').val(''); // remove the value from the input
            console.log(json); // log the returned json to the console
            $('#talk').prepend('<div class="content">Оставил пользователь:' + json.username + ' (' + json.first_name + ' ' + json.last_name + ') <div style="font-weight: 600; font-size: large">' + json.title + '</div>' + json.title_text + '<br>' + json.publication_date + '</div>');
            console.log("success"); // another sanity check
        },

        // handle a non-successful response
        error: function (xhr, errmsg, err) {
            //$('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
            //    " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(document.getElementById('film_name').innerHTML);
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
}