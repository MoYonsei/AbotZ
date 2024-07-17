$(document).ready(function() {
    var canvas = $('#botCanvas')[0];
    var ctx = canvas.getContext('2d');
    var actions = [];

    function getMousePos(canvas, event) {
        var rect = canvas.getBoundingClientRect();
        return {
            x: event.clientX - rect.left,
            y: event.clientY - rect.top
        };
    }

    $('#botCanvas').click(function(e) {
        var pos = getMousePos(canvas, e);
        var message = 'Mouse position: ' + pos.x + ',' + pos.y;
        console.log(message);
        // Add action to array
        actions.push({
            x: pos.x,
            y: pos.y,
            action: 'click' // Default action, can be expanded to include others
        });
    });

    $('#saveBtn').click(function() {
        console.log('Saving actions:', actions);
        // AJAX call to save actions
        $.ajax({
            url: '{% url "save_actions" %}',
            method: 'POST',
            data: JSON.stringify(actions),
            contentType: 'application/json',
            headers: {
                'X-CSRFToken': '{{ csrf_token }}'
            },
            success: function(response) {
                alert('Actions saved successfully!');
            },
            error: function(xhr, status, error) {
                console.error('Error saving actions:', error);
            }
        });
    });
});




$('#deleteModal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget); // Button that triggered the modal
    var botId = button.data('bot-id'); // Extract info from data-* attributes
    var botName = button.data('bot-name'); // Extract info from data-* attributes

    var modal = $(this);
    modal.find('#botName').text(botName);
    modal.find('#deleteForm').attr('action', '/delete_bot/' + botId + '/');
});



$(document).ready(function() {
    var botId;

    $('#deleteModal').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget); // Button that triggered the modal
        botId = button.data('bot-id'); // Extract info from data-* attributes
        var botName = button.data('bot-name'); // Extract info from data-* attributes

        var modal = $(this);
        modal.find('#botName').text(botName);
    });

    $('#confirmDeleteBtn').click(function() {
        $.ajax({
            url: '/delete_bot/' + botId + '/',
            type: 'DELETE',
            headers: {
                'X-CSRFToken': '{{ csrf_token }}'
            },
            success: function(result) {
                $('#deleteModal').modal('hide');
                $('#bot-' + botId).remove();
            },
            error: function(xhr, status, error) {
                console.error('Error deleting bot:', error);
            }
        });
    });
});
