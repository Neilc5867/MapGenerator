from MapGenerator import Terrain
import pytest

"""
" class Test
"
" Class for testing functionality of the MapGenerator's Terrain Objects.
"
"
"""
class Test(Terrain):
    # Test size constraints.
    def test_size_constraint(self):
        with pytest.raises(ValueError):
            ex1 = Terrain(600, "TestMap")
