const apikey = YOUR_API_KEY;

async function getWeather() {

    const city = document.getElementById("city").value.trim();

    if (!city) {
        alert("Please enter a city name");
        return;
    }

    const url = `https://api.weatherapi.com/v1/forecast.json?key=${apikey}&q=${city}&days=5&aqi=yes&alerts=yes`;

    try {

        const response = await fetch(url);
        const data = await response.json();

        if (data.error) {
            document.getElementById("weather").innerHTML = `
                <h3>${data.error.message}</h3>
            `;
            return;
        }

        renderCurrentWeather(data);
        renderHourly(data);
        renderForecast(data);

    } catch (error) {
        document.getElementById("weather").innerHTML = `
            <h3>Unable to fetch weather data.</h3>
        `;
    }
}

function renderCurrentWeather(data) {

    const weather = document.getElementById("weather");

    weather.innerHTML = `
        <h2>${data.location.name}, ${data.location.country}</h2>

        <img src="https:${data.current.condition.icon}" alt="Weather Icon">

        <h1>${data.current.temp_c}°C</h1>

        <p><b>${data.current.condition.text}</b></p>

        <div class="weather-details">

            <p>💧 Humidity : ${data.current.humidity}%</p>

            <p>🌬 Wind : ${data.current.wind_kph} km/h</p>

            <p>🌡 Feels Like : ${data.current.feelslike_c}°C</p>

            <p>🌿 AQI (PM2.5): ${data.current.air_quality.pm2_5.toFixed(2)}</p>

        </div>
    `;
}

function renderHourly(data) {

    const hourly = document.getElementById("hourly");

    hourly.innerHTML = "";

    const currentHour = new Date().getHours();

    const nextHours = data.forecast.forecastday[0].hour.slice(
        currentHour,
        currentHour + 8
    );

    nextHours.forEach(hour => {

        const time = hour.time.split(" ")[1];

        hourly.innerHTML += `
            <div class="hour-card">

                <p>${time}</p>

                <img src="https:${hour.condition.icon}" alt="">

                <h4>${hour.temp_c}°C</h4>

                <small>${hour.condition.text}</small>

            </div>
        `;

    });

}

function renderForecast(data) {

    const forecast = document.getElementById("forecast");

    forecast.innerHTML = "";

    // Skip today's weather
    data.forecast.forecastday.slice(1).forEach(day => {

        const dayName = new Date(day.date).toLocaleDateString("en-US", {
            weekday: "short"
        });

        forecast.innerHTML += `
            <div class="forecast-card">
                <h3>${dayName}</h3>
                <img src="https:${day.day.condition.icon}" alt="">
                <h2>${day.day.maxtemp_c}°C</h2>
                <p>Min: ${day.day.mintemp_c}°C</p>
                <p>${day.day.condition.text}</p>
                <small>🌧 ${day.day.daily_chance_of_rain}% Rain</small>
            </div>
        `;

    });

}