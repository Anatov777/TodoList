function editTask(id) {
    result = prompt('Изменение задачи', document.getElementById(id).getAttribute('title'));
    if (result) document.getElementById(id).setAttribute("href", document.getElementById(id).getAttribute('href')+"?editTextString="+result)
}
