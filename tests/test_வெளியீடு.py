import os.path
import tempfile
import unittest
from os import path

from தன்விவரங்கள் import தன்விவரங்கள்


class செய்தி_உருவாக்கம்(unittest.TestCase):
    def test_ஒடியெஃப்(தன்):
        நான் = தன்விவரங்கள்("த")
        நான்.பெயர்("நான் தான்")
        with tempfile.TemporaryDirectory() as கோப்புரை:
            நான்.வெளியிடு(வடிவூட்டம்="odt", கோப்புரை=கோப்புரை)
            தன்.assertTrue(os.path.isfile(path.join(கோப்புரை, "தன்விவரங்கள்_த.odt")))

    def test_pdf(தன்):
        நான் = தன்விவரங்கள்("த")
        நான்.பெயர்("நான் தான்")
        with tempfile.TemporaryDirectory() as கோப்புரை:
            try:
                நான்.வெளியிடு(வடிவூட்டம்="pdf", கோப்புரை=கோப்புரை)
            except FileNotFoundError:
                தன்.skipTest("soffice கிடைக்கவில்லை")
            தன்.assertTrue(os.path.isfile(path.join(கோப்புரை, "தன்விவரங்கள்_த.pdf")))
