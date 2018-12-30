import pytest

from loadpy.download import Download

# Dummy Data
DUMMY_URL = "https://content.jdmagicbox.com/comp/mumbai/w5/022pxx22.xx22.150516154322.z9w5/catalogue/blablacar-in-mumbai-online-websites-75wlg.jpg"

def test_core_count_is_not_zero():
    saveas = "A.jpg"
    m = Download(url=DUMMY_URL, filename=saveas)
    assert m.get_cores() > 0
