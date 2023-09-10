import random

import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Student, Course

# Фикстуры

@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


# Тесты

@pytest.mark.django_db
def test_course(client, course_factory):
    course = course_factory(_quantity=1)

    response = client.get('/api/v1/courses/1/')
    data = response.json()

    assert response.status_code == 200
    assert data['id'] == 1


@pytest.mark.django_db
def test_courses(client, course_factory):
    courses = course_factory(_quantity=10)

    response = client.get('/api/v1/courses/')
    data = response.json()

    assert response.status_code == 200

    for index, course in enumerate(data):
        assert courses[index].id == course['id']


@pytest.mark.django_db
def test_filter_id(client, course_factory):
    courses = course_factory(_quantity=1)

    response = client.get('/api/v1/courses/')
    data = response.json()

    assert response.status_code == 200

