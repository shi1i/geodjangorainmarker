// Функция для инициализации карты
function initMap() {
    var southWest = L.latLng(-85.0511287798, -180),
        northEast = L.latLng(85.0511287798, 180);
    var bounds = L.latLngBounds(southWest, northEast);

    var map = L.map('map', {
        attributionControl:false,
        maxBounds: bounds,
        maxBoundsViscosity: 1.0,
        minZoom: 3,
        zoomControl: false
    }).setView([45.03, 41.96], 13);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);
}

// Функция для переключения бокового меню
function toggleSidebar() {
    const sidebar = document.getElementById("sidebar");
    sidebar.style.width = sidebar.style.width === "250px" ? "0" : "250px";
}

// Функция для открытия модального окна
function openModal() {
    const modal = document.getElementById("modal");
    modal.style.display = "block"; // Показываем модальное окно
}

// Функция для закрытия модального окна
function closeModal() {
    const modal = document.getElementById("modal");
    modal.style.display = "none"; // Скрываем модальное окно
    document.getElementById("modalBody").innerHTML = ""; // Очищаем содержимое модального окна
}

// Функция для отображения формы входа
function showLoginForm() {
    document.getElementById("modalBody").innerHTML = document.getElementById("loginForm").innerHTML; // Загружаем содержимое формы входа
    openModal(); // Открываем модальное окно
}

// Функция для отображения формы регистрации
function showRegistrationForm() {
    document.getElementById("modalBody").innerHTML = document.getElementById("registrationForm").innerHTML; // Загружаем содержимое формы регистрации
    openModal(); // Открываем модальное окно
}

// Инициализация карты при загрузке страницы
document.addEventListener("DOMContentLoaded", initMap);
