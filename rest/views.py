'''
A interface não foi a renderização em um página web, mas através de API (serialização),
com necessidade de autehticação (TokenAuthentication)
'''

from rest_framework import viewsets, serializers, reverse, authentication, permissions
from .serializers import TarefaSerializer
from .models import Tarefa

# Create your views here.
class DefaultMixin(object):
    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    )

    permission_classes = (
        permissions.IsAuthenticated,
    )


class TarefaViewSet(DefaultMixin, viewsets.ModelViewSet):
    queryset = Tarefa.objects.order_by('id')
    serializer_class = TarefaSerializer
    links = serializers.SerializerMethodField()

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('produto-detail', kwargs={'pk': obj.pk},
                            request=request)
        }

