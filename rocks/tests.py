from django.core.urlresolvers import reverse
from django.test import TestCase
from django.utils import timezone

from .models import Rock


class RockViewsTest(TestCase):
    def setUp(self):
        self.rock = Rock.objects.create(
            name='Fake name',
            image_filename='fake.jpg',
            image_caption='fake caption',
            category='fake category',
            formula='fake formula',
            strunz_classification='fake strunz',
            crystal_system='fake crytal system',
            unit_cell='fake unit cell',
            color='fake color',
            crystal_symmetry='fake crystal symmetry',
            cleavage='fake cleavage',  # That's just funny.
            mohs_scale_hardness='fake Mohs',
            luster='fake luster',
            streak='fake streak',
            diaphaneity='fake diaphaneity',
            optical_properties='fake optical properties',
            refractive_index='fake refractive index',
            group='fake group',
            crystal_habit='fake crystal habit',
            specific_gravity='fake specific gravity'
            )

    def test_rock_index_view(self):
        resp = self.client.get(reverse('rocks:index'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.rock, resp.context['rocks'])

    def test_rock_detail_view(self):
        resp = self.client.get(reverse('rocks:detail', kwargs={'rock_name': self.rock.name}))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Fake Name')
