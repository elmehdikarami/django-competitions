# -*- coding: utf-8 -*-
from model_mommy import mommy

from django.test import TestCase

from .models import Gallery, Image, Thumbnail


class GalleryTest(TestCase):
    def test_gallery_creation(self):
        gallery = mommy.make(Gallery)
        self.assertTrue(isinstance(gallery, Gallery))
        self.assertEqual(gallery.__unicode__(), gallery.name)


class ImageTest(TestCase):
    def create_images(self, size):
        gallery = mommy.make(Gallery)
        images = mommy.make(Image, gallery=gallery, _quantity=size)        
        return images, gallery

    def test_creation(self):
        image = mommy.make(Image)        
        self.assertTrue(isinstance(image, Image))
        self.assertEqual(image.__unicode__(), image.url)

    def test_has_gallery(self):
        size = 3
        images, gallery = self.create_images(size)
        self.assertEqual(len(images), size)
        self.assertNotEqual(images[0].gallery, None)
        self.assertEqual(gallery.images.count(), size)


class ThumbnailTest(TestCase):
    def test_creation_thumbnail(self):
        thumb = mommy.make(Thumbnail)
        self.assertEqual(thumb.__unicode__(), thumb.name)
        self.assertEqual(thumb.to_url(), '%dx%d' % (thumb.width, thumb.height))
        self.assertEqual(thumb.to_thumbnail(), (thumb.height, thumb.width))
