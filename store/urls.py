from rest_framework_nested import routers

from . import views

router = routers.SimpleRouter()
router.register("products", views.ProductViewSet)
router.register("collections", views.CollectionViewSet)

products_router = routers.NestedDefaultRouter(router, "products", lookup="product")
products_router.register("reviews", views.ReviewViewSet, basename="product-reviews")

# ? URLConfigurations
urlpatterns = router.urls + products_router.urls
