from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from application.models import Chapter, Material, Subscription
from users.models import User


class ApplicationTestCaseCSU(APITestCase):
    def setUp(self) -> None:
        """Создание тестовых пользователя, раздела, материала, подписки"""
        self.user = User.objects.create(email="test_email", is_staff=True, is_superuser=True, password="123")
        self.client.force_authenticate(user=self.user)
        self.chapter = Chapter.objects.create(
            name="TestChapter",
            owner=self.user,
        )
        self.material = Material.objects.create(
            name="TestMaterial",
            owner=self.user,
            url="test@youtube.com",
            chapter=self.chapter,
        )
        self.subscription = Subscription.objects.create(
            subscriber=self.user,
            chapter=self.chapter,
        )

    def test_list_chapter(self) -> None:
        """Тестирование вывода списка разделов"""
        response = self.client.get("/chapter/")
        data = response.json()
        data["results"][0].pop("created")  # убираем автогенерируемую дату
        data["results"][0]["material"][0].pop("created")  # убираем автогенерируемую дату
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.chapter.id,
                    "material": [
                        {
                            "id": self.material.id,
                            "name": "TestMaterial",
                            "description": None,
                            "preview": None,
                            "url": self.material.url,
                            "chapter": self.material.chapter.id,
                            "owner": self.user.pk,
                        },
                    ],
                    "material_in_chapter_count": 1,
                    "is_subscribed": True,
                    "subscribers": [
                        {
                            "id": self.subscription.id,
                            "subscriber": self.user.pk,
                            "chapter": self.subscription.chapter.id,
                        },
                    ],
                    "name": self.chapter.name,
                    "description": self.chapter.description,
                    "preview": self.chapter.preview,
                    "owner": self.user.pk,
                }
            ],
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

    def test_create_chapter_csu(self) -> None:
        """Тестирование создания раздела"""
        data = {
            "name": "TestChapter2",
            "owner": self.user.pk,
        }

        response = self.client.post("/chapter/", data=data)
        data = response.json()
        data.pop("created")  # убираем автогенерируемую дату
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            data,
            {
                "id": response.json().get("id"),
                "material": [],
                "material_in_chapter_count": 0,
                "is_subscribed": False,
                "subscribers": [],
                "name": "TestChapter2",
                "description": None,
                "preview": None,
                "owner": self.user.pk,
            },
        )
        self.assertTrue(Chapter.objects.all().exists())

    def test_retrieve_chapter(self) -> None:
        """Тестирование вывода отдельного раздела"""
        response = self.client.get(f"/chapter/{self.chapter.pk}/")
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.chapter.name)

    def test_delete_chapter_csu(self) -> None:
        """Тестирование удаления раздела"""
        response = self.client.delete(f"/chapter/{self.chapter.pk}/")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Chapter.objects.all().count(), 0)

    def test_patch_chapter_csu(self) -> None:
        """Тестирование обновления раздела"""
        data = {
            "name": "TestChapter",
            "description": "TestDescription",
        }
        response = self.client.patch(f"/chapter/{self.chapter.pk}/", data=data)

        result = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result.get("description"), "TestDescription")

    def test_create_non_unique_chapter_name_csu(self) -> None:
        """Тестирование создания раздела с ошибкой в уникальности названия"""
        data = {
            "name": "TestChapter",
            "description": "TestDescription",
        }

        response = self.client.post("/chapter/", data=data)
        result = response.json()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(result, {"name": ["раздел with this Название already exists."]})

    def test_list_material(self) -> None:
        """Тестирование вывода списка материалов без указания раздела"""
        response = self.client.get("/material/")
        data = response.json()
        result: dict = {
            "count": 0,
            "next": None,
            "previous": None,
            "results": [],
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

    def test_list_chapter_material(self) -> None:
        """Тестирование вывода списка материалов с указанием раздела"""
        response = self.client.get(f"/material/?chapter={self.chapter.pk}")
        data = response.json()
        data["results"][0].pop("created")  # убираем автогенерируемую дату
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.material.id,
                    "name": self.material.name,
                    "description": None,
                    "preview": None,
                    "url": self.material.url,
                    "chapter": self.material.chapter.id,
                    "owner": self.user.pk,
                },
            ],
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

    def test_create_material(self) -> None:
        """Тестирование создания материала"""
        data = {
            "name": "TestMaterial",
            "chapter": self.chapter.pk,
            "url": "test@youtube.com",
            "owner": self.user.pk,
        }

        response = self.client.post("/material/", data=data)
        data = response.json()
        data.pop("created")  # убираем автогенерируемую дату
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            data,
            {
                "id": response.json().get("id"),
                "name": self.material.name,
                "description": None,
                "preview": None,
                "url": self.material.url,
                "chapter": self.material.chapter.id,
                "owner": self.user.pk,
            },
        )
        self.assertTrue(Material.objects.all().exists())

    def test_create_material_wrong_url(self) -> None:
        """Тестирование создания материала"""
        data = {
            "name": "TestMaterial",
            "chapter": self.chapter.pk,
            "url": "test@test.ru",
            "owner": self.user.pk,
        }

        response = self.client.post("/material/", data=data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(data, {"non_field_errors": ["Ссылка должна быть только с сервиса Youtube или отсутствовать"]})

    def test_retrieve_material_csu(self) -> None:
        """Тестирование вывода отдельного материала"""
        response = self.client.get(f"/material/{self.material.pk}/?chapter={self.chapter.pk}")
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.material.name)

    def test_delete_material_csu(self) -> None:
        """Тестирование удаления материала"""
        response = self.client.delete(f"/material/{self.material.pk}/?chapter={self.chapter.pk}")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Material.objects.all().count(), 0)

    def test_patch_material(self) -> None:
        """Тестирование обновления материала"""
        data = {
            "name": "TestMaterial",
            "description": "TestDescription",
        }
        response = self.client.patch(f"/material/{self.material.pk}/?chapter={self.chapter.pk}", data=data)

        result = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result.get("description"), "TestDescription")

    def test_create_subscription(self) -> None:
        """Тестирование создания подписки"""
        data = {
            "user": self.user.pk,
            "chapter": self.chapter.pk,
        }
        url = reverse("application:create_subscription")
        response = self.client.post(url, data=data)
        result_one = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result_one, {"message": "Вы отписались от Раздела с материалами"})
        self.assertEqual(Subscription.objects.all().count(), 0)

        response = self.client.post(url, data=data)
        result_two = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result_two, {"message": "Вы подписались на этот Раздел с материалами"})
        self.assertTrue(Subscription.objects.all().exists())

    def test_create_user(self) -> None:
        """Тестирование создания пользователя"""
        data = {
            "email": "test@mail.ru",
            "password": 12345678910,
        }
        url = reverse("users:register")
        response = self.client.post(url, data=data)
        result = response.json()
        result.pop("password")  # убираем пароль
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            result,
            {
                "id": 7,
                "is_superuser": False,
                "is_staff": False,
                "is_active": True,
                "email": "test@mail.ru",
                "groups": [],
            },
        )
        self.assertEqual(User.objects.all().count(), 2)
