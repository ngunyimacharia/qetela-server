from django.contrib.auth.models import User
from django.test import TestCase

from qetela.schema import schema

def initialize():
    user = User.objects.create_user("username","email@example.com","password")

class AccountGraphTests(TestCase):
    def test_users_without_user(self):
        query = '''
        query users {
            users{
                username,
                email
            }
        }
        '''
        expected = {
            "users": []
         }
        result = schema.execute(query)
        assert not result.errors
        assert result.data == expected

    def test_users_with_one_record(self):
        initialize()
        query = '''
        query users {
            users{
                username,
                email
            }
        }
        '''
        expected = {
            "users": [
              {
                "username": "username",
                "email": "email@example.com"
              }
            ]
         }
        result = schema.execute(query)
        assert not result.errors
        assert result.data == expected

    def test_get_user(self):
        initialize()
        query = '''
        query user{
            user(username:"username"){
                username,
                email
            }
        }
        '''
        expected = {
                "user": {
                  "username": "username",
                  "email": "email@example.com"
                }
        }
        result = schema.execute(query)
        assert not result.errors
        assert result.data == expected

    def test_adding_user(self):
        mutation = '''
        mutation createUser {
            createUser(
                username: "username",
                firstName: "FirstName",
                lastName: "LastName"
                email: "email@example.com",
                password: "password",
                cPassword: "password",
            ){
                username,
                email,
                firstName,
                lastName
            }
        }
        '''
        expected = {
            "createUser": {
              "username": "username",
              "email": "email@example.com",
              "firstName": "FirstName",
              "lastName": "LastName"
            }
        }
        result = schema.execute(mutation)
        assert not result.errors
        assert result.data == expected

    def test_updating_user(self):
        initialize()
        mutation = '''
        mutation updateUser {
            updateUser(
                username:"username",
                nUsername:"updated",
                email:"newemail@example.com",
                firstName:"NewFName",
                lastName:"NewLName",
                password:"newpassword",
                cPassword:"newpassword",
            ){
                username,
                email,
                firstName,
                lastName
            }
        }
        '''
        expected = {
            "updateUser": {
              "username": "updated",
              "email": "newemail@example.com",
              "firstName": "NewFName",
              "lastName": "NewLName"
            }
        }
        result = schema.execute(mutation)
        assert not result.errors
        assert result.data == expected

    def test_delete_user(self):
        initialize()
        mutation = '''
        mutation deleteUser {
            deleteUser(username:"username"){
                ok
            }
        }
        '''
        expected = {
            "deleteUser": {
              "ok": True
            }
        }
        result = schema.execute(mutation)
        assert not result.errors
        assert result.data == expected
