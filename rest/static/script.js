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

function addUser(button)
{
    var children = $(button).parent().children();
    var name = children.eq(0).val();
    var phone = children.eq(1).val();
    var data = JSON.stringify({'name': name, 'phone': phone});
    
    $.ajax({
        'url': '/users',
        'type': 'POST',
        'contentType': 'application/json',
        'data': data,
        'dataType': 'json',
        'error': ajaxError,
        'success': ajaxSuccess
    });
}

function updateUser(button, userId)
{
    var children = $(button).parent().children();
    var name = children.eq(0).val();
    var phone = children.eq(1).val();
    var data = JSON.stringify({'name': name, 'phone': phone});
    
    $.ajax({
        'url': '/users/' + userId,
        'type': 'PUT',
        'contentType': 'application/json',
        'data': data,
        'dataType': 'json',
        'error': ajaxError,
        'success': ajaxSuccess
    });
}

function deleteUser(button, userId)
{
    var children = $(button).parent().children();
    var data = JSON.stringify({});
    
    $.ajax({
        'url': '/users/' + userId,
        'type': 'DELETE',
        'contentType': 'application/json',
        'data': data,
        'dataType': 'json',
        'error': ajaxError,
        'success': ajaxSuccess
    });

}