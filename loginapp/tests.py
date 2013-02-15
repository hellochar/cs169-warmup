"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from loginapp.models import UsersModel

from django.conf import settings


class SimpleTest(TestCase):

    def testAdd1(self):
        """
        Tests that adding a user works
        """
        self.assertEquals(settings.STATUS_CODES['SUCCESS'], UsersModel.add("user1", "password"))

    def testAddExists(self):
        """
        Tests that adding a duplicate user name fails
        """
        self.assertEquals(settings.STATUS_CODES['SUCCESS'], UsersModel.add("user1", "password"))
        self.assertEquals(settings.STATUS_CODES['ERR_USER_EXISTS'], UsersModel.add("user1", "password"))

    def testAdd2(self):
        """
        Tests that adding two users works
        """
        self.assertEquals(settings.STATUS_CODES['SUCCESS'], UsersModel.add("user1", "password"))
        self.assertEquals(settings.STATUS_CODES['SUCCESS'], UsersModel.add("user2", "password"))

    def testAddEmptyUsername(self):
        """
        Tests that adding an user with empty username fails
        """
        self.assertEquals(settings.STATUS_CODES['ERR_BAD_USERNAME'], UsersModel.add("", "password"))

    def testUsernameTooLong(self):
        username = "name"*100
        self.assertEquals(settings.STATUS_CODES['ERR_BAD_USERNAME'], UsersModel.add(username, "password"))

    def testPasswordTooLong(self):
        password = "pass"*100
        self.assertEquals(settings.STATUS_CODES['ERR_BAD_PASSWORD'], UsersModel.add('user', password))

    def testInitialCountIs1(self):
        UsersModel.add("user1", "password")
        self.assertEquals(1, UsersModel.objects.get(user="user1").count)

    def testLoginIncrementsCount(self):
        UsersModel.add("user1", "password")
        UsersModel.login('user1', "password")
        self.assertEquals(2, UsersModel.objects.get(user="user1").count)

    def testUsersHaveSeparateCounts(self):
        UsersModel.add("user1", "password")
        UsersModel.add("user2", "password")

        UsersModel.login('user1', "password")
        UsersModel.login('user1', "password")
        UsersModel.login('user2', "password")

        self.assertEquals(3, UsersModel.objects.get(user="user1").count)
        self.assertEquals(2, UsersModel.objects.get(user="user2").count)

    def testLoginExists(self):
        self.assertEquals(settings.STATUS_CODES['ERR_BAD_CREDENTIALS'], UsersModel.login('baduser', 'password'));

