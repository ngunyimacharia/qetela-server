from organisations.models import Organisation as OrganisationModel
import graphene

class CreateOrganisationMutation(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    website = graphene.String()
    branches = graphene.Boolean()
    cf_frequency = graphene.Int()
    created = graphene.types.datetime.DateTime()
    updated = graphene.types.datetime.DateTime()

    class Arguments:
        id = graphene.Int()
        name = graphene.String(required=True)
        website = graphene.String()
        branches = graphene.Boolean()
        cf_frequency = graphene.Int()
        created = graphene.types.datetime.DateTime()
        updated = graphene.types.datetime.DateTime()

    def mutate(self, info, name, **org_data):
        website = org_data.get('website', None)
        branches = org_data.get('branches', False)
        cf_frequency = org_data.get('cf_frequency', 7)
        organisation = OrganisationModel(name=name,website=website,branches=branches,cf_frequency=cf_frequency)
        organisation.save()
        return CreateOrganisationMutation(id=organisation.id,name=organisation.name,website=organisation.website,branches=organisation.branches,cf_frequency=organisation.cf_frequency,created=organisation.created,updated=organisation.updated)


class UpdateOrganisationMutation(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    website = graphene.String()
    branches = graphene.Boolean()
    cf_frequency = graphene.Int()
    created = graphene.types.datetime.DateTime()
    updated = graphene.types.datetime.DateTime()

    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String()
        website = graphene.String()
        branches = graphene.Boolean()
        cf_frequency = graphene.Int()
        created = graphene.types.datetime.DateTime()
        updated = graphene.types.datetime.DateTime()

    def mutate(self, info, id, **org_data):

        organisation = OrganisationModel.objects.get(pk=id)

        for k,v in org_data.items():
            setattr(organisation,k,v)

        organisation.save()

        return UpdateOrganisationMutation(id=id,name=organisation.name,website=organisation.website,branches=organisation.branches,cf_frequency=organisation.cf_frequency,created=organisation.created,updated=organisation.updated)


class DeleteOrganisationMutation(graphene.Mutation):
    id = graphene.Int()
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, id):

        organisation = OrganisationModel.objects.get(pk=id)
        result = organisation.delete()
        return DeleteOrganisationMutation(ok=result)


class OrganisationMutations(graphene.ObjectType):
    create_organisation = CreateOrganisationMutation.Field()
    update_organisation = UpdateOrganisationMutation.Field()
    delete_organisation = DeleteOrganisationMutation.Field()
