from django.contrib.auth.models import User
from organisations.models import Organisation,Level,Team,Position
from django.test import TestCase
from .models import UserPosition
from .seeder import gen_users

from qetela.schema import schema

def initialize():
    organisation = Organisation(
        id=1,
        name='Test'
    )
    organisation.save()
    level = Level(
        id=1,
        label='Test',
        number=1,
        organisation=organisation
    )
    level.save()
    team = Team(
        id=1,
        name='Test',
        active=True,
        level=level
    )
    team.save()
    position = Position(
        id=1,
        title='Test',
        description='Test description',
        team = team
    )
    position.save()
    position2 = Position(
        id=2,
        title='Test Position 2',
        description='Test description',
        team = team
    )
    position2.save()
    user = User.objects.create_user("username","email@example.com","password")
    organisation.users.add(user)
    up = UserPosition(id=1,user=user,position=position,start="2019-01-01")
    up.save()

class UserGraphTests(TestCase):
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
            user(email:"email@example.com"){
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

class UserPositionTests(TestCase):
    def test_users_with_up(self):
        initialize()
        query = '''
        query users {
          users{
            username,
            userpositionSet{
              position{
                title,
              }
              start,
              stop
            }
          }
        }
        '''
        expected = {
            "users": [
              {
                "username": "username",
                "userpositionSet": [
                  {
                    "position": {
                      "title": "Test",
                    },
                    "start": "2019-01-01",
                    "stop": None
                  }
                 ]
              }
            ]
         }
        result = schema.execute(query)
        assert not result.errors
        assert result.data == expected

    def test_adding_up(self):
        initialize()
        mutation = '''
            mutation createUserPosition{
              createUserPosition(username:"username",positionId:2,start:"2018-02-12"){
                username,
                positionTitle,
                start,
                stop
              }
            }
        '''
        expected = {
            "createUserPosition": {
              "username": "username",
              "positionTitle": "Test Position 2",
              "start": "2018-02-12",
              "stop": None
            }
        }
        result = schema.execute(mutation)
        assert not result.errors
        assert result.data == expected


    def test_updating_up(self):
        initialize()
        mutation = '''
            mutation updateUserPosition{
              updateUserPosition(id:1,stop:"2019-03-19"){
                stop
              }
            }
        '''
        expected = {
            "updateUserPosition": {
              "stop":"2019-03-19"
            }
        }
        result = schema.execute(mutation)
        assert not result.errors
        assert result.data == expected


    def test_delete_up(self):
        initialize()
        mutation = '''
        mutation deleteUserPosition {
            deleteUserPosition(id:1){
                ok
            }
        }
        '''
        expected = {
            "deleteUserPosition": {
              "ok": True
            }
        }
        result = schema.execute(mutation)
        assert not result.errors
        assert result.data == expected

class AccountSeederTest(TestCase):
    def test_seeder(self):
        gen_users()
        assert Position.objects.all().count() < User.objects.all().count()
