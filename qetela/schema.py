from organisations.models import Organisation as OrganisationModel
from graphene_django.types import DjangoObjectType
import graphene

class Organisation(DjangoObjectType):
    class Meta:
        model = OrganisationModel


class Query(graphene.ObjectType):
    organisation = graphene.Field(Organisation,id=graphene.ID(required=True))
    organisations = graphene.List(Organisation)

    def resolve_organisation(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return OrganisationModel.objects.get(pk=id)
        return None

    def resolve_organisations(self, info, **kwargs):
        return OrganisationModel.objects.all()

class CreateOrganisationMutation(graphene.Mutation):
    name = graphene.String()
    website = graphene.String()
    branches = graphene.Boolean()
    cf_frequency = graphene.Int()

    class Arguments:
        name = graphene.String(required=True)
        website = graphene.String()
        branches = graphene.Boolean()
        cf_frequency = graphene.Int()

    def mutate(self, info, name, **org_data):
        website = org_data.get('website', None)
        branches = org_data.get('branches', False)
        cf_frequency = org_data.get('cf_frequency', 7)
        organisation = OrganisationModel(name=name,website=website,branches=branches,cf_frequency=cf_frequency)
        organisation.save()
        return CreateOrganisationMutation(name=name,website=website,branches=branches,cf_frequency=cf_frequency)


class UpdateOrganisationMutation(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    website = graphene.String()
    branches = graphene.Boolean()
    cf_frequency = graphene.Int()

    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String()
        website = graphene.String()
        branches = graphene.Boolean()
        cf_frequency = graphene.Int()

    def mutate(self, info, id, **org_data):

        organisation = OrganisationModel.objects.get(pk=id)

        for k,v in org_data.items():
            setattr(organisation,k,v)

        organisation.save()

        return UpdateOrganisationMutation(id=id,name=organisation.name,website=organisation.website,branches=organisation.branches,cf_frequency=organisation.cf_frequency)


class DeleteOrganisationMutation(graphene.Mutation):
    id = graphene.Int()
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, id):

        organisation = OrganisationModel.objects.get(pk=id)
        result = organisation.delete()
        return DeleteOrganisationMutation(ok=result)


class Mutation(graphene.ObjectType):
    create_organisation = CreateOrganisationMutation.Field()
    update_organisation = UpdateOrganisationMutation.Field()
    delete_organisation = DeleteOrganisationMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
