import json
from django.shortcuts import render
from graphene_file_upload.utils import place_files_in_operations
from graphql_extensions.views import GraphQLView


def robots(request):
    http_host = request.get_host()
    if http_host is not None and http_host.startswith("dev.pycon.kr"):
        return render(request, 'dev-robots.txt', content_type='text/plain')
    return render(request, 'robots.txt', content_type='text/plain')


class PyConGraphQLView(GraphQLView):
    def parse_body(self, request):
        """Handle multipart request spec for multipart/form-data"""
        content_type = self.get_content_type(request)
        if content_type == 'multipart/form-data':
            operations = json.loads(request.POST.get('operations', '{}'))
            files_map = json.loads(request.POST.get('map', '{}'))
            return place_files_in_operations(
                operations,
                files_map,
                request.FILES
            )
        return super(PyConGraphQLView, self).parse_body(request)
