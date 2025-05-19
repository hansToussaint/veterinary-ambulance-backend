from django.http import HttpResponse, JsonResponse
from .models import *
from django.shortcuts import get_object_or_404
import json

# === Vets ===
def return_all_vets(request):
    vets = Vets.objects.all()
    return JsonResponse(list(vets.values()), safe=False)

def create_vet(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            vet = Vets.objects.create(
                name=data['name'],
                specialization=data.get('specialization', '')
            )
            return JsonResponse({"id": vet.id, "name": vet.name, "specialization": vet.specialization}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)
    return HttpResponse('This is a POST only endpoint!', status=405)

def delete_vet(request, vet_id):
    vet = get_object_or_404(Vets, pk=vet_id)
    vet.delete()
    return HttpResponse(f'Vet with id {vet_id} was deleted!', status=200)

def update_vet(request, vet_id):
    if request.method == 'PATCH':
        vet = get_object_or_404(Vets, pk=vet_id)
        data = json.loads(request.body)
        for field, value in data.items():
            if hasattr(vet, field):
                setattr(vet, field, value)
        vet.save()
        return JsonResponse({"id": vet.id, "name": vet.name, "specialization": vet.specialization})
    return HttpResponse('This is a PATCH only endpoint!', status=405)


# === Appointments ===
def return_all_appointments(request):
    appointments = Appointments.objects.all().select_related('pet', 'vet')
    data = [{"id": a.id, "date": a.date, "pet": a.pet_id, "vet": a.vet_id} for a in appointments]
    return JsonResponse(data, safe=False)

def create_appointment(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            appointment = Appointments.objects.create(
                date=data['date'],
                pet_id=data.get('pet'),
                vet_id=data.get('vet')
            )
            return JsonResponse({"id": appointment.id, "date": appointment.date, "pet": appointment.pet_id, "vet": appointment.vet_id}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)
    return HttpResponse('This is a POST only endpoint!', status=405)

def delete_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointments, pk=appointment_id)
    appointment.delete()
    return HttpResponse(f'Appointment with id {appointment_id} was deleted!', status=200)

def update_appointment(request, appointment_id):
    if request.method == 'PATCH':
        appointment = get_object_or_404(Appointments, pk=appointment_id)
        data = json.loads(request.body)
        for field, value in data.items():
            if hasattr(appointment, field):
                setattr(appointment, field, value)
        appointment.save()
        return JsonResponse({"id": appointment.id, "date": appointment.date, "pet": appointment.pet_id, "vet": appointment.vet_id})
    return HttpResponse('This is a PATCH only endpoint!', status=405)


# === Vaccines ===
def return_all_vaccines(request):
    vaccines = Vaccines.objects.all()
    return JsonResponse(list(vaccines.values()), safe=False)

def create_vaccine(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            vaccine = Vaccines.objects.create(
                name=data['name'],
                description=data.get('description', '')
            )
            return JsonResponse({"id": vaccine.id, "name": vaccine.name, "description": vaccine.description}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)
    return HttpResponse('This is a POST only endpoint!', status=405)

def delete_vaccine(request, vaccine_id):
    vaccine = get_object_or_404(Vaccines, pk=vaccine_id)
    vaccine.delete()
    return HttpResponse(f'Vaccine with id {vaccine_id} was deleted!', status=200)

def update_vaccine(request, vaccine_id):
    if request.method == 'PATCH':
        vaccine = get_object_or_404(Vaccines, pk=vaccine_id)
        data = json.loads(request.body)
        for field, value in data.items():
            if hasattr(vaccine, field):
                setattr(vaccine, field, value)
        vaccine.save()
        return JsonResponse({"id": vaccine.id, "name": vaccine.name, "description": vaccine.description})
    return HttpResponse('This is a PATCH only endpoint!', status=405)


# === Pet Vaccines ===
def return_all_pet_vaccines(request):
    pet_vaccines = PetVaccines.objects.all().select_related('pet', 'vaccine')
    data = [{"id": pv.id, "pet": pv.pet_id, "vaccine": pv.vaccine_id, "time_of_vaccination": pv.time_of_vaccination} for pv in pet_vaccines]
    return JsonResponse(data, safe=False)

def create_pet_vaccine(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            pet_vaccine = PetVaccines.objects.create(
                pet_id=data.get('pet'),
                vaccine_id=data.get('vaccine'),
                time_of_vaccination=data.get('time_of_vaccination')
            )
            return JsonResponse({"id": pet_vaccine.id, "pet": pet_vaccine.pet_id, "vaccine": pet_vaccine.vaccine_id, "time_of_vaccination": pet_vaccine.time_of_vaccination}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)
    return HttpResponse('This is a POST only endpoint!', status=405)

def delete_pet_vaccine(request, pet_vaccine_id):
    pet_vaccine = get_object_or_404(PetVaccines, pk=pet_vaccine_id)
    pet_vaccine.delete()
    return HttpResponse(f'Pet Vaccine with id {pet_vaccine_id} was deleted!', status=200)

def create_pet(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        pet = Pets.objects.create(
            name = data['name'],
            species = data.get('species'),
            age = data.get('age'),
            owner_id = data.get('owner_id')
        )

        return JsonResponse({
            "id": pet.id,
            "name": pet.name,
            "species": pet.species,
            "age": pet.age,
            "owner_id": pet.owner_id
        })
    else:
        return HttpResponse('This is a POST only endpoint!', status=405)

def delete_pet(request, pet_id):
    if request.method == 'DELETE':
        pet = get_object_or_404(Pets, pk=pet_id)

        pet.delete()

        return HttpResponse(f'Pet with id {pet_id} was deleted!', status=200)
    else:
        return HttpResponse('This is a DELETE only endpoint!', status=405)

def update_pet(request, pet_id):
    if request.method == 'PATCH':
        pet = get_object_or_404(Pets, pk=pet_id)
        data = json.loads(request.body)

        if 'name' in data:
            pet.name = data['name']

        if 'species' in data:
            pet.species = data['species']

        if 'age' in data:
            pet.age = data['age']

        if 'owner_id' in data:
            pet.owner_id = data['owner_id']

        pet.save()

        return JsonResponse({
            "id": pet.id,
            "name": pet.name,
            "species": pet.species,
            "age": pet.age,
            "owner_id": pet.owner_id
        })
    else:
        return HttpResponse('This is a PATCH only endpoint!', status=405)

def update_owner(request, owner_id):
    if request.method == 'PATCH':
        owner = get_object_or_404(Owners, pk=owner_id)
        data = json.loads(request.body)

        if 'name' in data:
            owner.name = data['name']

        if 'phone' in data:
            owner.phone = data['phone']

        owner.save()

        return JsonResponse({
            "id": owner.id,
            "name": owner.name,
            "phone": owner.phone
        })
    else:
        return HttpResponse('This is a PATCH only endpoint!', status=405)
    
def delete_owner(request, owner_id):
    if request.method == 'DELETE':
        owner = get_object_or_404(Owners, pk=owner_id)

        owner.delete()

        return HttpResponse(f'Owner with id {owner_id} was deleted!', status=200)
    else:
        return HttpResponse('This is a DELETE only endpoint!', status=405)

def create_owner(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        owner = Owners.objects.create(
            name = data['name'],
            phone = data['phone']
        )

        return JsonResponse({
            "id": owner.id,
            "name": owner.name,
            "phone": owner.phone
        })
    else:
        return HttpResponse('This is a POST only endpoint!', status=405)

def return_all_pets_by_owner(request, owner_id):
    owner = get_object_or_404(Owners, pk=owner_id)

    pets = Pets.objects.filter(owner=owner)

    pets_serialized = []

    for pet in pets:
        pets_serialized.append(
            {
                "id": pet.id,
                "name": pet.name,
                "species": pet.species,
                "age": pet.age
            }
        )
    
    return JsonResponse({
        "owner_id": owner_id,
        "owner_name": owner.name,
        "owner_phone": owner.phone,
        "pets": pets_serialized
    })

def return_all_owners(request):
    owners = Owners.objects.all()
    owners_serialized = []

    for owner in owners:
        owners_serialized.append(
            {
                "id": owner.id,
                "name": owner.name,
                "phone": owner.phone
            }
        )

    print(owners_serialized)

    return JsonResponse(owners_serialized, safe=False)

def simple_test(request):
    return HttpResponse('Hello World, this is the test page!')

def simple_post_test(request):
    if request.method == 'POST':
        decoded_data = request.body.decode('utf-8')
        print(decoded_data)
        return HttpResponse('Data was received!')
    else:
        return HttpResponse('This is a POST only endpoint!', status=405)