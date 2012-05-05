/**
 * on load
 */
$(document).ready(function(){
    /**
     * check on ie
     */
    if ($.browser.msie) {
        alert("Internet Explorer doesn't support");
    }
    /**
     * send message from quick form
     */
    $('#quick-submit').live('click',function(){
       $.ajax({
            type : "POST",
            url  : "/ajax/quick-form",
            data : ({
                'csrfmiddlewaretoken' : $('[name="csrfmiddlewaretoken"]').val(),
                'name'                : $('[name="name"]').val(),
                'email'               : $('[name="email"]').val(),
                'message'             : $('[name="message"]').val()
            }),
            success: function(msg){
                alert(msg);
            }
        });
    });
    /**
     * get tweets for social activity
     */
    $.getJSON('http://api.twitter.com/1/statuses/user_timeline.json?screen_name=d1ffuz0r&page=1&count=3&callback=?',
        function(data) {
            var container = $('#activity-tweets');
            $(data).each(function(i, tweet) {
                var text = tweet.text.replace(/(http\S+)/gi, '<a href="$1" target="_blank">$1</a>');
                container.append('<li>' + text + '</li>');
            });
        }
    );
});