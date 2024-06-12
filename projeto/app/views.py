import io
import csv
from django.http import FileResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UploadFileForm, BiomaAmazoniaForm, BiomaCerradoForm, BiomaCaatingaForm, BiomaPampaForm, BiomaPantanalForm, BiomaMataAtlanticaForm
from . models import BiomaAmazonia, BiomaCerrado, BiomaCaatinga, BiomaPampa, BiomaPantanal, BiomaMataAtlantica

# Create your views here.

def home(request):
    return render(request, 'home.html')

def listar_amazonia(request):
    Amazonia = BiomaAmazonia.objects.all()
    return render(request, 'listar_amazonia.html',{'Amazonia':Amazonia})

def readBiomaCerrado(request):
    Cerrado = BiomaCerrado.objects.all()
    return render(request, 'readBiomaCerrado.html',{'Cerrado':Cerrado})

def readBiomaCaatinga(request):
    Caatinga = BiomaCaatinga.objects.all()
    return render(request, 'readBiomaCaatinga.html',{'Caatinga':Caatinga})

def readBiomaPampa(request):
    Pampa = BiomaPampa.objects.all()
    return render(request, 'readBiomaPampa.html',{'Pampa':Pampa})

def readBiomaPantanal(request):
    Pantanal = BiomaPantanal.objects.all()
    return render(request, 'readBiomaPantanal.html',{'Pantanal':Pantanal})

def readBiomaMataAtlantica(request):
    MataAtlantica = BiomaMataAtlantica.objects.all()
    return render(request, 'readBiomaMataAtlantica.html',{'MataAtlantica':MataAtlantica})

def deleteBiomaAmazonia(request, id):
    Amazonia = get_object_or_404(BiomaAmazonia, pk=id)
    Amazonia.delete()
    return redirect("readBiomaAmazonia")

def deleteBiomaCerrado(request, id):
    Cerrado = get_object_or_404(BiomaCerrado, pk=id)
    Cerrado.delete()
    return redirect("readBiomaCerrado")

def deleteBiomaCaatinga(request, id):
    Caatinga = get_object_or_404(BiomaCaatinga, pk=id)
    Caatinga.delete()
    return redirect("readBiomaCaatinga")

def deleteBiomaPampa(request, id):
    Pampa = get_object_or_404(BiomaPampa, pk=id)
    Pampa.delete()
    return redirect("readBiomaPampa")

def deleteBiomaPantanal(request, id):
    Pantanal = get_object_or_404(BiomaPantanal, pk=id)
    Pantanal.delete()
    return redirect("readBiomaPantanal")

def deleteBiomaMataAtlantica(request, id):
    MataAtlantica = get_object_or_404(BiomaMataAtlantica, pk=id)
    MataAtlantica.delete()
    return redirect("readBiomaMataAtlantica")

def BiomaAmazonia_import(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            reader = csv.DictReader(io.StringIO(request.FILES["file"].read().decode('utf-8')))
            for row in reader:
                print("row")
                print(row)
                BiomaAmazonia.objects.create(
                    maxima=row['maxima'],
                    media=row['media'],
                    minima=row['minima'],
                    anos=row['ano'],
                    total=row['Total'],
                    janeiro=row['Janeiro'],
                    fevereiro=row['Fevereiro'],
                    marco=row['Marco'],
                    abril=row['Abril'],
                    maio=row['Maio'],
                    junho=row['Junho'],
                    julho=row['Julho'],
                    agosto=row['Agosto'],
                    setembro=row['Setembro'],
                    outubro=row['Outubro'],
                    novembro=row['Novembro'],
                    dezembro=row['Dezembro'])

            return redirect("listar_amazonia")
    else:
        form = UploadFileForm()
        return render(request, 'importarDados.html', {'form':form})

def BiomaCerrado_import(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            reader = csv.DictReader(io.StringIO(request.FILES["file"].read().decode('utf-8')))
            for row in reader:
                print("row")
                print(row)
                BiomaCerrado.objects.create(
                    maxima=row['maxima'],
                    media=row['media'],
                    minima=row['minima'],
                    anos=row['ano'],
                    total=row['Total'],
                    janeiro=row['Janeiro'],
                    fevereiro=row['Fevereiro'],
                    marco=row['Marco'],
                    abril=row['Abril'],
                    maio=row['Maio'],
                    junho=row['Junho'],
                    julho=row['Julho'],
                    agosto=row['Agosto'],
                    setembro=row['Setembro'],
                    outubro=row['Outubro'],
                    novembro=row['Novembro'],
                    dezembro=row['Dezembro'])

            return redirect("listar_BiomaCerrado")
    else:
        form = UploadFileForm()
        return render(request, 'importarDados.html', {'form':form})

def BiomaCaatinga_import(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            reader = csv.DictReader(io.StringIO(request.FILES["file"].read().decode('utf-8')))
            for row in reader:
                print("row")
                print(row)
                BiomaCaatinga.objects.create(
                    maxima=row['maxima'],
                    media=row['media'],
                    minima=row['minima'],
                    anos=row['ano'],
                    total=row['Total'],
                    janeiro=row['Janeiro'],
                    fevereiro=row['Fevereiro'],
                    marco=row['Marco'],
                    abril=row['Abril'],
                    maio=row['Maio'],
                    junho=row['Junho'],
                    julho=row['Julho'],
                    agosto=row['Agosto'],
                    setembro=row['Setembro'],
                    outubro=row['Outubro'],
                    novembro=row['Novembro'],
                    dezembro=row['Dezembro'])

            return redirect("listar_BiomaCaatinga")
    else:
        form = UploadFileForm()
        return render(request, 'importarDados.html', {'form':form})

def BiomaPampa_import(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            reader = csv.DictReader(io.StringIO(request.FILES["file"].read().decode('utf-8')))
            for row in reader:
                print("row")
                print(row)
                BiomaPampa.objects.create(
                    maxima=row['maxima'],
                    media=row['media'],
                    minima=row['minima'],
                    anos=row['ano'],
                    total=row['Total'],
                    janeiro=row['Janeiro'],
                    fevereiro=row['Fevereiro'],
                    marco=row['Marco'],
                    abril=row['Abril'],
                    maio=row['Maio'],
                    junho=row['Junho'],
                    julho=row['Julho'],
                    agosto=row['Agosto'],
                    setembro=row['Setembro'],
                    outubro=row['Outubro'],
                    novembro=row['Novembro'],
                    dezembro=row['Dezembro'])

            return redirect("listar_BiomaPampa")
    else:
        form = UploadFileForm()
        return render(request, 'importarDados.html', {'form':form})

def BiomaPantanal_import(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            reader = csv.DictReader(io.StringIO(request.FILES["file"].read().decode('utf-8')))
            for row in reader:
                print("row")
                print(row)
                BiomaPantanal.objects.create(
                    maxima=row['maxima'],
                    media=row['media'],
                    minima=row['minima'],
                    anos=row['ano'],
                    total=row['Total'],
                    janeiro=row['Janeiro'],
                    fevereiro=row['Fevereiro'],
                    marco=row['Marco'],
                    abril=row['Abril'],
                    maio=row['Maio'],
                    junho=row['Junho'],
                    julho=row['Julho'],
                    agosto=row['Agosto'],
                    setembro=row['Setembro'],
                    outubro=row['Outubro'],
                    novembro=row['Novembro'],
                    dezembro=row['Dezembro'])

            return redirect("listar_BiomaPantanal")
    else:
        form = UploadFileForm()
        return render(request, 'importarDados.html', {'form':form})

def BiomaMataAtlantica_import(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            reader = csv.DictReader(io.StringIO(request.FILES["file"].read().decode('utf-8')))
            for row in reader:
                print("row")
                print(row)
                BiomaMataAtlantica.objects.create(
                    maxima=row['maxima'],
                    media=row['media'],
                    minima=row['minima'],
                    anos=row['ano'],
                    total=row['Total'],
                    janeiro=row['Janeiro'],
                    fevereiro=row['Fevereiro'],
                    marco=row['Marco'],
                    abril=row['Abril'],
                    maio=row['Maio'],
                    junho=row['Junho'],
                    julho=row['Julho'],
                    agosto=row['Agosto'],
                    setembro=row['Setembro'],
                    outubro=row['Outubro'],
                    novembro=row['Novembro'],
                    dezembro=row['Dezembro'])

            return redirect("listar_BiomaMataAtlantica")
    else:
        form = UploadFileForm()
        return render(request, 'importarDados.html', {'form':form})

def downloadCSVBiomaAmazonia(request):
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=BiomaAmazonia.csv'

    writer = csv.writer(response)
    writer.writerow([
        'maxima', 'media', 'minima', 'anos', 'total', 'janeiro', 'fevereiro', 'marco', 'abril', 'maio',
        'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])

    dados = BiomaAmazonia.objects.all().values_list(
        'maxima', 'media', 'minima', 'anos', 'total', 'janeiro', 'fevereiro', 'marco', 'abril', 'maio',
        'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')

    for dado in dados:
        writer.writerow(dado)

    return response

def downloadCSVBiomaCerrado(request):
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=BiomaCerrado.csv'

    writer = csv.writer(response)
    writer.writerow([
        'maxima', 'media', 'minima', 'anos', 'total', 'janeiro', 'fevereiro', 'marco', 'abril', 'maio',
        'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])

    dados = BiomaCerrado.objects.all().values_list(
        'maxima', 'media', 'minima', 'anos', 'total', 'janeiro', 'fevereiro', 'marco', 'abril', 'maio',
        'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')

    for dado in dados:
        writer.writerow(dado)

    return response

def downloadCSVBiomaCaatinga(request):
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=BiomaCaatinga.csv'

    writer = csv.writer(response)
    writer.writerow([
        'maxima', 'media', 'minima', 'anos', 'total', 'janeiro', 'fevereiro', 'marco', 'abril', 'maio',
        'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])

    dados = BiomaCaatinga.objects.all().values_list(
        'maxima', 'media', 'minima', 'anos', 'total', 'janeiro', 'fevereiro', 'marco', 'abril', 'maio',
        'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')

    for dado in dados:
        writer.writerow(dado)

    return response

def downloadCSVBiomaPampa(request):
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=BiomaPampa.csv'

    writer = csv.writer(response)
    writer.writerow([
        'maxima', 'media', 'minima', 'anos', 'total', 'janeiro', 'fevereiro', 'marco', 'abril', 'maio',
        'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])

    dados = BiomaPampa.objects.all().values_list(
        'maxima', 'media', 'minima', 'anos', 'total', 'janeiro', 'fevereiro', 'marco', 'abril', 'maio',
        'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')

    for dado in dados:
        writer.writerow(dado)

    return response

def downloadCSVBiomaPantanal(request):
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=BiomaPantanal.csv'

    writer = csv.writer(response)
    writer.writerow([
        'maxima', 'media', 'minima', 'anos', 'total', 'janeiro', 'fevereiro', 'marco', 'abril', 'maio',
        'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])

    dados = BiomaPantanal.objects.all().values_list(
        'maxima', 'media', 'minima', 'anos', 'total', 'janeiro', 'fevereiro', 'marco', 'abril', 'maio',
        'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')

    for dado in dados:
        writer.writerow(dado)

    return response

def downloadCSVBiomaMataAtlantica(request):
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=BiomaMataAtlantica.csv'

    writer = csv.writer(response)
    writer.writerow([
        'maxima', 'media', 'minima', 'anos', 'total', 'janeiro', 'fevereiro', 'marco', 'abril', 'maio',
        'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])

    dados = BiomaMataAtlantica.objects.all().values_list(
        'maxima', 'media', 'minima', 'anos', 'total', 'janeiro', 'fevereiro', 'marco', 'abril', 'maio',
        'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')

    for dado in dados:
        writer.writerow(dado)

    return response

def downloadBiomaAmazonia(request, pk):
    Amazonia = get_object_or_404(BiomaAmazonia, pk=pk)
    response = FileResponse(Amazonia.arquivo)
    return response

