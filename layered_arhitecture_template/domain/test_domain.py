import unittest

from layered_arhitecture_template.domain.entity1 import Entity1
from layered_arhitecture_template.domain.entity2 import Entity2
from layered_arhitecture_template.domain.validators import Entity1Validator, Entity1ValidatorException, \
    Entity2Validator, Entity2ValidatorException


class TestEntity1(unittest.TestCase):
    def test_entity1(self):
        item = Entity1(1, "abc", 20)
        self.assertEqual(item.attribute1, 1)
        self.assertEqual(item.attribute2, "abc")
        self.assertEqual(item.attribute3, 20)

    def test_attribute3_setter(self):
        item = Entity1(20, "a", 1000)
        item.attribute3 = -100
        self.assertEqual(item.attribute3, -100)

    def test_str(self):
        item = Entity1(1, "abc", 20)
        self.assertEqual("attribute1: 1, attribute2: abc, attribute3: 20", item.__str__())


class TestEntity1Validator(unittest.TestCase):
    def test_entity1_validator(self):
        val = Entity1Validator()
        # entity1 invalid if attribute1 is not int
        entity1 = Entity1("abc", "lll", 17)
        try:
            val.validate(entity1)
            assert False
        except Entity1ValidatorException:
            pass

        # entity1 invalid if attribute1 is lower than 0
        entity1 = Entity1(-1, "lll", 17)
        try:
            val.validate(entity1)
            assert False
        except Entity1ValidatorException:
            pass


class TestEntity2(unittest.TestCase):
    def test_entity2_getters(self):
        item = Entity2(1, "zz", 19)
        self.assertEqual(item.attribute1, 1)
        self.assertEqual(item.attribute2, "zz")
        self.assertEqual(item.attribute3, 19)

    def test_entity2_setters(self):
        item = Entity2(1, "zz", 19)
        try:
            item.attribute1 = 5
            self.assertFalse("attribute1 was set, though it should not have happened")
        except AttributeError as aerror:
            self.assertTrue(str(aerror) == "can't set attribute")

        item.attribute2 = "m"
        item.attribute3 = 2
        self.assertNotEqual(item.attribute1, 5)
        self.assertEqual(item.attribute2, "m")
        self.assertEqual(item.attribute3, 2)

    def test_str(self):
        item = Entity2(1, "abc", 20)
        self.assertEqual("attribute1: 1, attribute2: abc, attribute3: 20", item.__str__())


class TestEntity2Validator(unittest.TestCase):
    def test_entity2_validator(self):
        val = Entity2Validator()
        # entity2 invalid if attribute1 is not int
        entity2 = Entity2("", "abc", 12)
        try:
            val.validate(entity2)
            assert False
        except Entity2ValidatorException:
            pass

        # entity2 invalid if attribute1 lower than 1
        entity2 = Entity2(0, "xyz", all)
        try:
            val.validate(entity2)
            assert False
        except Entity2ValidatorException:
            pass

