from django.urls import path
from .views import *

urlpatterns = [

    # Owners
    path('owners/', return_all_owners),
    path('owners/<int:owner_id>/pets/', return_all_pets_by_owner),
    path('owners/create', create_owner),
    path('owners/delete/<int:owner_id>', delete_owner),
    path('owners/update/<int:owner_id>', update_owner),

    # Pets
    path('pets/create', create_pet),
    path('pets/delete/<int:pet_id>', delete_pet),
    path('pets/update/<int:pet_id>', update_pet),

    # Vets
    path('vets/', return_all_vets),
    path('vets/create', create_vet),
    path('vets/delete/<int:vet_id>', delete_vet),
    path('vets/update/<int:vet_id>', update_vet),

    # Appointments
    path('appointments/', return_all_appointments),
    path('appointments/create', create_appointment),
    path('appointments/delete/<int:appointment_id>', delete_appointment),
    path('appointments/update/<int:appointment_id>', update_appointment),

    # Vaccines
    path('vaccines/', return_all_vaccines),
    path('vaccines/create', create_vaccine),
    path('vaccines/delete/<int:vaccine_id>', delete_vaccine),
    path('vaccines/update/<int:vaccine_id>', update_vaccine),

    # Pet Vaccines
    path('pet-vaccines/', return_all_pet_vaccines),
    path('pet-vaccines/create', create_pet_vaccine),
    path('pet-vaccines/delete/<int:pet_vaccine_id>', delete_pet_vaccine),
]
