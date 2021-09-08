from .v1.views import HealthView, RootViews, APIViews, APIViewsGet

routers = [
    ("/", RootViews()),
    ("/health", HealthView()),
    ("/api/car/create", APIViews()),
    ("/api/car/consult", APIViewsGet()),
]
