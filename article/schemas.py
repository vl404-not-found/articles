import graphql_jwt
import graphene
from django.db.models import Q
from graphene_django import DjangoObjectType
from graphql_jwt.decorators import login_required

from article.models import Article


class ArticleType(DjangoObjectType):
    class Meta:
        model = Article


class Query(graphene.ObjectType):
    article = graphene.Field(ArticleType, id=graphene.UUID())

    @login_required
    def resolve_article(self, info, **kwargs):
        ident = kwargs.get('id')
        # slug = kwargs.get('slug')
        if ident is not None:
            return Article.objects.get(pk=ident)


class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
