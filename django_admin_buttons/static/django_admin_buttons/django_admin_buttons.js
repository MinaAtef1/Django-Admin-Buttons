function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function button_action(id, action) {
    form = document.createElement('form');
    form.setAttribute('method', 'post');
    form.setAttribute('action', window.location.href);
  
    action_input = document.createElement('input');
    action_input.setAttribute('type', 'hidden');
    action_input.setAttribute('name', 'action');
    action_input.setAttribute('value', action);
    form.appendChild(action_input);
    
    id_input = document.createElement('input');
    id_input.setAttribute('type', 'hidden');
    id_input.setAttribute('name', '_selected_action');
    id_input.setAttribute('value', id);
    form.appendChild(id_input);
  
  
    csrf_input = document.createElement('input');
    csrf_input.setAttribute('type', 'hidden');
    csrf_input.setAttribute('name', 'csrfmiddlewaretoken');
    csrf_input.setAttribute('value', getCookie('csrftoken'));
    form.appendChild(csrf_input);
  
    document.body.appendChild(form);
    form.submit();
  }
  