from django.db.models import Transform

class Unaccent(Transform):
    lookup_name = 'unaccent'

    def as_sql(self, qn, connection):
        lhs, params = qn.compile(self.lhs)
        return "UNACCENT(%s)" % lhs, params
