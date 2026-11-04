// Icon mapping for Visual Crossing icons
const iconMap = {
    'clear-day': '☀️',
    'clear-night': '🌙',
    'rain': '🌧️',
    'snow': '❄️',
    'sleet': '🌨️',
    'wind': '💨',
    'fog': '🌫️',
    'cloudy': '☁️',
    'partly-cloudy-day': '⛅',
    'partly-cloudy-night': '☁️',
    'hail': '🌨️',
    'thunderstorm': '⛈️',
    'thunderstorm-rain': '⛈️',
    'thunderstorm-snow': '⛈️'
};

async function fetchWeather(city) {
    loading.classList.remove('hidden');
    weatherCard.classList.add('hidden');

    try {
        const response = await fetch(`/weather?city=${encodeURIComponent(city)}`);
        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || 'Failed to fetch weather');
        }

        displayWeather(data);
    } catch (err) {
        showError(err.message);
    } finally {
        loading.classList.add('hidden');
    }
}

function displayWeather(data) {
    document.getElementById('cityName').textContent = data.address || data.city;
    document.getElementById('description').textContent = data.description || data.conditions;
    document.getElementById('temperature').textContent = `${data.temperature}°C`;
    document.getElementById('feelsLike').textContent = `${data.feels_like}°C`;
    document.getElementById('humidity').textContent = `${data.humidity}%`;
    document.getElementById('windSpeed').textContent = `${data.wind_speed} km/h`;

    const icon = iconMap[data.icon] || '🌤️';
    const weatherIcon = document.getElementById('weatherIcon');
    weatherIcon.textContent = icon;
    weatherIcon.style.fontSize = '64px';

    weatherCard.classList.remove('hidden');
}

function showError(message) {
    errorDiv.textContent = message;
    errorDiv.classList.remove('hidden');
}

const cityInput = document.getElementById('cityInput');
const searchBtn = document.getElementById('searchWeatherBtn');
const loading = document.getElementById('loading');
const errorDiv = document.getElementById('error');
const weatherCard = document.getElementById('weatherCard');

searchBtn.addEventListener('click', () => {
    const city = cityInput.value.trim();
    if (city) {
        fetchWeather(city);
    }
});

cityInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        const city = cityInput.value.trim();
        if (city) {
            fetchWeather(city);
        }
    }
});

