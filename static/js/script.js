const container = document.getElementById('container');
const registerBtn = document.getElementById('register');
const loginBtn = document.getElementById('login');

registerBtn.addEventListener('click', () => {
    container.classList.add("active");
});

loginBtn.addEventListener('click', () => {
    container.classList.remove("active");
});



document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('create-chat').addEventListener('click', function () {
      alert('Создание нового чата!');
      // Тут можно вставить логику создания чата
    });
  
    document.getElementById('enter-chat').addEventListener('click', function () {
      alert('Вход в чат!');
      // Тут можно вставить логику входа в существующий чат
    });
  });
  