import unittest
import os
import testLib
import testSimple

# class TestAddUser(testLib.RestTestCase):
class TestAdd(testSimple.TestAddUser):
    """
    test different count for multiple users logging in
    """
    def testMultipleUsers(self):
        self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        self.makeRequest("/users/add", method="POST", data = { 'user' : 'user2', 'password' : 'password'} )

        user1_respData = self.makeRequest('/users/login', method="POST", data = { 'user' : 'user1', 'password' : 'password'} )

        self.makeRequest('/users/login', method="POST", data = { 'user' : 'user2', 'password' : 'password'} )
        user2_respData = self.makeRequest('/users/login', method="POST", data = { 'user' : 'user2', 'password' : 'password'} )

        self.assertResponse(user1_respData, count = 2)
        self.assertResponse(user2_respData, count = 3)

    """
    test duplicate add not working
    """
    def testDuplicateAdd(self):
        self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        dup_respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )

        self.assertResponse(dup_respData, None, testLib.RestTestCase.ERR_USER_EXISTS)

    """
    test bad username and subsequently not being able to log in
    """
    def testBadUsername(self):
        self.makeRequest("/users/add", method="POST", data = { 'user' : 'username' * 128, 'password' : 'password' })
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : 'username' * 128, 'password' : 'password' })
        self.assertNotEqual(1, respData['errCode'])

    """
    test bad password and subsequently not being able to log in
    """
    def testBadPassword(self):
        self.makeRequest("/users/add", method="POST", data = { 'user' : 'username', 'password' : 'password' * 128 })
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : 'username', 'password' : 'password' * 128 })
        self.assertNotEqual(1, respData['errCode'])

class TestLogin(testSimple.TestAddUser):
    """
    test count incrementing on login
    """
    def testCountIncrements(self):
        self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'password' } )

        self.makeRequest("/users/login", method="POST", data = { 'user' : 'user1', 'password' : 'password' } )
        self.makeRequest("/users/login", method="POST", data = { 'user' : 'user1', 'password' : 'password' } )
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : 'user1', 'password' : 'password' } )

        self.assertResponse(respData, 4)

    """
    test login on non-existent user erroring
    """
    def testLoginUserNotExist(self):
        respData = self.makeRequest("/users/login", method="POST", data = {'user' : 'baduser', 'password' : 'password' } )
        self.assertResponse(respData, None, testLib.RestTestCase.ERR_BAD_CREDENTIALS)
