import fakeredis
from mock import patch
from django.test import TestCase
from ..views import CacheMixin


class TestRedisViews(TestCase):
    def setUp(self):
        redis_patcher = patch(CacheMixin, fakeredis.FakeRedis)
        print(redis_patcher)
        self.redis = redis_patcher.start()

    def tearDown(self):
        self.redis_patcher.stop