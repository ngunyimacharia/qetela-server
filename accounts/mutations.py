from django.contrib.auth.models import User as UserModel
import graphene


class CreateUserMutation(graphene.Mutation):
    id = graphene.Int()
    username = graphene.String()
    first_name = graphene.String()
    last_name = graphene.String()
    email = graphene.String()
    password = graphene.String()
    c_password = graphene.String()
    is_active = graphene.Boolean()
    date_joined = graphene.types.datetime.DateTime()
    last_login = graphene.types.datetime.DateTime()

    class Arguments:
        username = graphene.String(required=True)
        first_name = graphene.String()
        last_name = graphene.String()
        email = graphene.String(required=True)
        password = graphene.String(required=True)
        c_password = graphene.String(required=True)
        is_active = graphene.Boolean()

    def mutate(self, info, username, email, password, c_password, **kwargs):
        #check if username is taken
        if UserModel.objects.filter(username=username).count():
            raise ValueError("Username is already being used")

        #check if email is taken
        if UserModel.objects.filter(email=email).count():
            raise ValueError("Email is already being used")
        # check passwords
        if password != c_password:
            raise ValueError("Passwords do not match")
        user = UserModel.objects.create_user(username, email, password)
        for k,v in kwargs.items():
            setattr(user,k,v)
        user.save()
        return CreateUserMutation(
            id=user.id,
            username = user.username,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            is_active=user.is_active,
            date_joined=user.date_joined,
            last_login=user.last_login,

        )


class UpdateUserMutation(graphene.Mutation):
    id = graphene.Int()
    username = graphene.String()
    first_name = graphene.String()
    last_name = graphene.String()
    email = graphene.String()
    password = graphene.String()
    c_password = graphene.String()
    is_active = graphene.Boolean()
    date_joined = graphene.types.datetime.DateTime()
    last_login = graphene.types.datetime.DateTime()

    class Arguments:
        username = graphene.String(required=True)
        n_username = graphene.String()
        first_name = graphene.String()
        last_name = graphene.String()
        email = graphene.String()
        password = graphene.String()
        c_password = graphene.String()
        is_active = graphene.Boolean()

    def mutate(self, info, username, **kwargs):
        #get user being updated
        user = UserModel.objects.get(username=username)
        # check if usename is being updated
        n_username = kwargs.get('n_username',None)
        if n_username:
            if UserModel.objects.filter(username=n_username).count():
                raise ValueError("Username is already being used")
            else:
                user.username = n_username
        # check if password is being updated
        password = kwargs.get('password',None)
        c_password = kwargs.get('c_password',None)
        if password and c_password:
            if password == c_password:
                user.set_password(password)
            else:
                raise ValueError("Passwords do not match")
        elif password or c_password:
            raise ValueError("Both password and password confirmation are required")

        for k,v in kwargs.items():
            if k == 'n_username' or k == 'password' or k == 'c_password':
                continue
            setattr(user,k,v)
        user.save()
        return UpdateUserMutation(
            id=user.id,
            username = user.username,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            is_active=user.is_active,
            date_joined=user.date_joined,
            last_login=user.last_login,

        )


class DeleteUserMutation(graphene.Mutation):
    username = graphene.String()
    ok = graphene.Boolean()

    class Arguments:
        username = graphene.String(required=True)

    def mutate(self, info, username):

        user = UserModel.objects.get(username=username)
        result = user.delete()
        return DeleteUserMutation(ok=result)


class AccountMutations(graphene.ObjectType):
    create_user = CreateUserMutation.Field()
    update_user = UpdateUserMutation.Field()
    delete_user = DeleteUserMutation.Field()
