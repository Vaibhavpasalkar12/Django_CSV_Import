from .models import EmpD
from import_export import resources

class EmpDResource(resources.ModelResource):
    class Meta:
        model = EmpD