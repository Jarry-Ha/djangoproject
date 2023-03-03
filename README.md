# Django Tutorial Code

Django Tutorial Code By Jarry

## Tutorial URL

- https://docs.djangoproject.com/ko/4.1/intro/install/
- https://docs.djangoproject.com/ko/4.1/intro/tutorial01/
- https://docs.djangoproject.com/ko/4.1/intro/tutorial02/
- https://docs.djangoproject.com/ko/4.1/intro/tutorial03/
- https://docs.djangoproject.com/ko/4.1/intro/tutorial04/
  - Commit before section(Use generic views)
  - Commit Using generic views
- https://docs.djangoproject.com/ko/4.1/intro/tutorial05/
  - TDD 환경 만들기
- https://velog.io/@may_soouu/Django-%EB%A9%94%EC%86%8C%EB%93%9C-%EC%A0%95%EB%A6%AC
  - Django 메소드 정리
- https://docs.djangoproject.com/ko/4.1/intro/tutorial06/
- https://docs.djangoproject.com/en/4.1/intro/tutorial07/

## Shell Command

### Shell에서 Test 환경 만들기

```bash
$ python manage.py shell
>>> # 환경셋팅하기
>>> from django.test.utils import setup_test_environment
>>> setup_test_environment()
>>> # create an instance of the client for our use
>>> from django.test import Client
>>> client = Client()
>>> # get a response from '/'
>>> response = client.get('/')
>>> # we should expect a 404 from that address; if you instead see an
>>> # "Invalid HTTP_HOST header" error and a 400 response, you probably
>>> # omitted the setup_test_environment() call described earlier.
>>> response.status_code
>>> # on the other hand we should expect to find something at '/polls/'
>>> # we'll use 'reverse()' rather than a hardcoded URL
>>> from django.urls import reverse
>>> response = client.get(reverse('polls:index'))
>>> response.status_code
>>> response.content
>>> response.context['latest_question_list']
```
