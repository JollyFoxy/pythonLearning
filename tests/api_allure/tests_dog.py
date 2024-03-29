import allure
import pytest


@allure.feature('Random dog')
@allure.story('Получение фото случайной собаки и вложенные друг в друга шаги')
def test_get_random_dog(dog_base_url):
    response = dog_base_url.get("breeds/image/random", None, None)

    with allure.step("Отпраляем запрос"):
        assert response.status_code == 200, f"Неверный код ответа, получен {response.status_code}"

    with allure.step("Парсим json-ниниу и проверяем статус"):
        response = response.json()
        assert response["status"] == "success"

    with allure.step("шаг внутри"):
        with allure.step("внутренний шаг в нутри которого ещё шаг"):
            with allure.step("Самый внутрений шаг"):
                pass


@allure.feature('Random dog')
@allure.story('Фото случайной собаки из определенной породы')
@pytest.mark.parametrize("breed", ["afghan",
                                   "basset", "blood", "english",
                                   "ibizan", "plott", "walker"])
def test_get_random(dog_base_url, breed):
    response = dog_base_url.get(f"breed/hound/{breed}/images/random")
    response = response.json()
    assert breed in response["message"], f"Нет ссылки на изображение с указанной породой, ответ {response}"


@allure.feature('List of dog images')
@allure.story('Список всех фото собак списком содержит только изображения')
@pytest.mark.parametrize("file", ['.md', '.MD', '.exe', '.txt'])
def test_get_breed_images(dog_base_url, file):
    response = dog_base_url.get("breed/hound/images")
    response = response.json()
    result = '\n'.join(response["message"])
    assert file not in result, f"В сообщении есть файл с расширением {file}"


@allure.feature('List of dog images')
@allure.story('Список определенного количества случайных фото')
@allure.feature('List of dog images')
@allure.story('Список фото определенных пород')
@pytest.mark.parametrize("breed", ["african", "boxer",
                                   "entlebucher", "elkhound", "shiba",
                                   "whippet", "spaniel", "dvornyaga"])
def test_get_random_breed_images(dog_base_url, breed):
    response = dog_base_url.get(f"breed/{breed}/images/")
    response = response.json()
    assert response["status"] == "success", f"Не удалось получить список изображений породы {breed}"


@pytest.mark.parametrize("number_of_images", [i for i in range(1, 10)])
def test_get_few_sub_breed_random_images(dog_base_url, number_of_images):
    response = dog_base_url.get(f"breed/hound/afghan/images/random/{number_of_images}")
    response = response.json()
    final_len = len(response["message"])
    assert final_len == number_of_images, f"Количество фото не {number_of_images}, а {final_len}"
