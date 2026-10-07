# Сергей Андреев, 48-я когорта — Финальный проект. Инженер по тестированию плюс

import pytest

result = pytest.main(["-v", "get_order_by_track_test.py"])

if result == 0:
    print("Тест пройден")
else:
    print("Тест провален")
