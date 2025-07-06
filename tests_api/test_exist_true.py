import requests
import pytest
import os

# Базовый URL API берется из переменных окружения или использует значение по умолчанию
AUTH_CHECK_ENDPOINT = os.getenv("AUTH_CHECK_ENDPOINT", "http://localhost:3000/exist")

def test_check_autorized():
    headers = {
        "Content-Type": "application/json",
        "Authorization": os.getenv("AUTH_TOKEN")  # Токен берется из переменных окружения
    }
    payload = {
        "email": os.getenv("USER_EMAIL", "user100@example.com")  # Email из окружения или значение по умолчанию
    }
    
    response = requests.post(AUTH_CHECK_ENDPOINT, headers=headers, json=payload)
    response_json = response.json()
    
    # Проверки ответа
    assert "exist" in response_json
    assert response.status_code == 200
    assert response_json["exist"] is False