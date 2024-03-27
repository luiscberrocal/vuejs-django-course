from django.test import TestCase

from vuejs_django_course.calisthenics.tests.factories import HitFactory


class TestHitFactory(TestCase):

    def test_hit_factory(self):
        hits = HitFactory.create_batch(5)
        self.assertEqual(len(hits), 5)
        for hit in hits:
            print(hit.date)
            self.assertIsNotNone(hit.exercise)
            self.assertIsNotNone(hit.date)
            self.assertIsNotNone(hit.reps)
            self.assertIsNotNone(hit.weight)
            self.assertIsNotNone(hit.user)
            self.assertTrue(hit.reps > 0)
            self.assertTrue(hit.weight > 0)
            self.assertTrue(hit.user.is_active)
