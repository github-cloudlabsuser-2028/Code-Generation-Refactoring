const axios = require('axios');

const API_KEY = 'd1ad1ee81341f423ba3fd13c48d9d12b';  // Replace with your OpenWeatherMap API key
const BASE_URL = 'http://api.openweathermap.org/data/2.5/weather';

async function getWeather(city) {
    try {
        const response = await axios.get(BASE_URL, {
            params: {
                q: city,
                appid: API_KEY,
                units: 'metric'  // Use 'imperial' for Fahrenheit
            }
        });
        const data = response.data;
        return {
            city: data.name,
            temperature: data.main.temp,
            description: data.weather[0].description
        };
    } catch (error) {
        return null;
    }
}

async function main() {
    const city = process.argv[2];
    if (!city) {
        console.log("Please provide a city name.");
        return;
    }
    const weather = await getWeather(city);
    if (weather) {
        console.log(`City: ${weather.city}`);
        console.log(`Temperature: ${weather.temperature}°C`);
        console.log(`Weather: ${weather.description}`);
    } else {
        console.log("City not found or API request failed.");
    }
}

main();