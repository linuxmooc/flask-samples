function ajaxError()
{
    alert('ajax error');
}

function ajaxSuccess(result)
{
    if (result.error) {
        alert('操作失败');
        return;
    }
    location.reload();
}

function onAddTodo(button)
{
    var children = $(button).parent().children();
    var title = children.eq(0).val();
    var data = JSON.stringify({'title': title});

    $.ajax({
        'url': '/todos/add',
        'type': 'POST',
        'contentType': 'application/json',
        'data': data,
        'dataType': 'json',
        'error': ajaxError,
        'success': ajaxSuccess
    });
}

function onUpdateTodo(todoId) 
{
    var data = JSON.stringify({'todoId': todoId});
    
    $.ajax({
        'url': '/todos/update',
        'type': 'POST',
        'contentType': 'application/json',
        'data': data,
        'dataType': 'json',
        'error': ajaxError,
        'success': ajaxSuccess
    });
}

function onDeleteTodo(todoId)
{
    var data = JSON.stringify({'todoId': todoId});

    $.ajax({
        'url': '/todos/delete',
        'type': 'POST',
        'contentType': 'application/json',
        'data': data,
        'dataType': 'json',
        'error': ajaxError,
        'success': ajaxSuccess
    });
}
