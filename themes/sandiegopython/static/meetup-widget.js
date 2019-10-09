// Meetup widget
//
// Display upcoming SD Python events in the sidebar
// Load the meetup widget if there is a div for it (#meetup-widget)
$(document).ready(function () {
    var WIDGET_CONTAINER = "#meetup-widget";

    if ($(WIDGET_CONTAINER).length) {
        $.ajax({
            dataType: "html",
            url: "https://www.pythonsd.org/meetup-widget.html",
            success: function (data) {
                $(WIDGET_CONTAINER).append(data);
            }
        });
    }
});
