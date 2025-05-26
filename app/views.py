import io
import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from .filters import BiomaFilter
from django.http import FileResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UploadFileForm, BiomaAmazoniaForm, BiomaCerradoForm, BiomaCaatingaForm, BiomaPampaForm, BiomaPantanalForm, BiomaMataAtlanticaForm
from . models import Amazonia, Cerrado, Caatinga, Pampa, Pantanal, MataAtlantica

# Create your views here.

def home(request):
    return render(request, 'home.html')

def importar_dados(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            bioma = form.cleaned_data['bioma']
            reader = csv.DictReader(io.StringIO(request.FILES["file"].read().decode('utf-8')))

            if bioma == 'BiomaAmazonia':
                model = Amazonia
            elif bioma == 'BiomaCerrado':
                model = Cerrado
            elif bioma == 'BiomaCaatinga':
                model = Caatinga
            elif bioma == 'BiomaPampa':
                model = Pampa
            elif bioma == 'BiomaPantanal':
                model = Pantanal
            elif bioma == 'BiomaMataAtlantica':
                model = MataAtlantica

            for row in reader:
                model.objects.create(
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
                    dezembro=row['Dezembro']
                )

            return redirect("listar_{}".format(bioma.lower()))
    else:
        form = UploadFileForm()
    return render(request, 'importar_dados.html', {'form': form})

def listar_amazonia(request):
    Amazonia = Amazonia.objects.all()
    return render(request, 'listar_amazonia.html',{'Amazonia':Amazonia})

def listar_cerrado(request):
    Cerrado = Cerrado.objects.all()
    return render(request, 'listar_cerrado.html',{'Cerrado':Cerrado})

def listar_caatinga(request):
    Caatinga = Caatinga.objects.all()
    return render(request, 'listar_caatinga.html',{'Caatinga':Caatinga})

def listar_pampa(request):
    Pampa = Pampa.objects.all()
    return render(request, 'listar_pampa.html',{'Pampa':Pampa})

def listar_pantanal(request):
    Pantanal = Pantanal.objects.all()
    return render(request, 'listar_pantanal.html',{'Pantanal':Pantanal})

def listar_atlantica(request):
    MataAtlantica = MataAtlantica.objects.all()
    return render(request, 'listar_atlantica.html',{'MataAtlantica':MataAtlantica})

def delete_amazonia(request, id):
    Amazonia = get_object_or_404(BiomaAmazonia, pk=id)
    Amazonia.delete()
    return redirect("listar_amazonia")

def delete_cerrado(request, id):
    Cerrado = get_object_or_404(BiomaCerrado, pk=id)
    Cerrado.delete()
    return redirect("listar_cerrado")

def delete_caatinga(request, id):
    Caatinga = get_object_or_404(BiomaCaatinga, pk=id)
    Caatinga.delete()
    return redirect("listar_caatinga")

def delete_pampa(request, id):
    Pampa = get_object_or_404(BiomaPampa, pk=id)
    Pampa.delete()
    return redirect("listar_pampa")

def delete_pantanal(request, id):
    Pantanal = get_object_or_404(BiomaPantanal, pk=id)
    Pantanal.delete()
    return redirect("listar_pantanal")

def delete_atlantica(request, id):
    MataAtlantica = get_object_or_404(BiomaMataAtlantica, pk=id)
    MataAtlantica.delete()
    return redirect("listar_atlantica")

"""def BiomaAmazonia_import(request):
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
        return render(request, 'importar_dados.html', {'form':form})

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
        return render(request, 'importar_dados.html', {'form':form})

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
        return render(request, 'importar_dados.html', {'form':form})

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
        return render(request, 'importar_dados.html', {'form':form})

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
        return render(request, 'importar_dados.html', {'form':form})

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
        return render(request, 'importar_dados.html', {'form':form})"""

def downloadCSVBiomaAmazonia(request):
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=BiomaAmazonia.csv'

    writer = csv.writer(response)
    writer.writerow([
        'maxima', 'media', 'minima', 'anos', 'total', 'janeiro', 'fevereiro', 'marco', 'abril', 'maio',
        'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])

    dados = Amazonia.objects.all().values_list(
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

    dados = Cerrado.objects.all().values_list(
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

    dados = Caatinga.objects.all().values_list(
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

    dados = Pampa.objects.all().values_list(
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

    dados = Pantanal.objects.all().values_list(
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

    dados = MataAtlantica.objects.all().values_list(
        'maxima', 'media', 'minima', 'anos', 'total', 'janeiro', 'fevereiro', 'marco', 'abril', 'maio',
        'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')

    for dado in dados:
        writer.writerow(dado)

    return response

def downloadBiomaAmazonia(request, pk):
    Amazonia = get_object_or_404(Amazonia, pk=pk)
    response = FileResponse(Amazonia.arquivo)
    return response

def seletor_bioma(bioma_name):
    biomas = {
        'Amazônia': Amazonia,
        'Cerrado': Cerrado,
        'Caatinga': Caatinga,
        'Pampa': Pampa,
        'Pantanal': Pantanal,
        'Mata Atlântica': MataAtlantica,
    }
    return biomas.get(bioma_name)

# Função para obter dados do bioma selecionado
def obter_dados(bioma_model):
    dados = bioma_model.objects.all()
    df = pd.DataFrame(list(dados.values()))
    meses = ['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
    for mes in meses:
        df[mes] = pd.to_numeric(df[mes], errors='coerce')
    return df

# Função para filtrar bioma e retornar a visualização com gráfico
def filtrar_bioma(request):
    filterset = BiomaFilter(request.GET or None)
    bioma_data = None
    bioma_name = None

    if filterset.is_valid():
        bioma_name = filterset.cleaned_data.get('Bioma')
        bioma_model = seletor_bioma(bioma_name)
        if bioma_model:
            bioma_data = obter_dados(bioma_model)

    context = {
        'filterset': filterset,
        'bioma_data': bioma_data,
        'bioma_name': bioma_name,
    }
    return render(request, 'filtrar_bioma.html', context)

# Função para plotar a série histórica
def serie_historica(df, bioma_name):
    # Definição dos dados para o gráfico
    anos = df['anos']
    total = df[['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']].sum(axis=1)

    # Criação do gráfico
    plt.figure(figsize=(10, 6))
    plt.plot(anos, total, marker='o', linestyle='-', label=f'Total de Focos Ativos - {bioma_name}')

    # Configurações do gráfico
    plt.title(f'Total de Focos Ativos Detectados por Mês de cada Ano - {bioma_name}')
    plt.xlabel('Ano')
    plt.ylabel('Total de Focos Ativos')
    plt.grid(True)
    plt.legend()

    # Exibição do gráfico
    plt.tight_layout()
    plt.xticks(rotation=45)
    plt.show()

def grafico_comparativo_biomas():
    # Obter dados de todos os biomas
    dados_amazonia = obter_dados(Amazonia)
    dados_cerrado = obter_dados(Cerrado)
    dados_caatinga = obter_dados(Caatinga)
    dados_pampa = obter_dados(Pampa)
    dados_pantanal = obter_dados(Pantanal)
    dados_atlantica = obter_dados(MataAtlantica)

    # Lista de DataFrames e nomes dos biomas
    biomas = [
        (dados_amazonia, 'Amazônia'),
        (dados_cerrado, 'Cerrado'),
        (dados_caatinga, 'Caatinga'),
        (dados_pampa, 'Pampa'),
        (dados_pantanal, 'Pantanal'),
        (dados_atlantica, 'Mata Atlântica'),
    ]

    plt.figure(figsize=(12, 8))

    for df, nome in biomas:
        # Calcular total de focos ativos para cada ano
        df['total'] = df[['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']].sum(axis=1)
        plt.plot(df['anos'], df['total'], label=nome)

    # Configurações do gráfico
    plt.title('Comparativo dos Focos Ativos entre Biomas')
    plt.xlabel('Ano')
    plt.ylabel('Total de Focos Ativos')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.xticks(rotation=45)
    plt.show()

# Chamada para gerar o gráfico comparativo entre biomas
grafico_comparativo_biomas()

def grafico_pizza_biomas():
    # Obter dados de todos os biomas
    dados_amazonia = obter_dados(Amazonia)
    dados_cerrado = obter_dados(Cerrado)
    dados_caatinga = obter_dados(Caatinga)
    dados_pampa = obter_dados(Pampa)
    dados_pantanal = obter_dados(Pantanal)
    dados_atlantica = obter_dados(MataAtlantica)

    # Lista de DataFrames e nomes dos biomas
    biomas = [
        (dados_amazonia, 'Amazônia'),
        (dados_cerrado, 'Cerrado'),
        (dados_caatinga, 'Caatinga'),
        (dados_pampa, 'Pampa'),
        (dados_pantanal, 'Pantanal'),
        (dados_atlantica, 'Mata Atlântica'),
    ]

    totais = []
    nomes = []

    for df, nome in biomas:
        # Calcular total de focos ativos para cada bioma
        total = df[['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']].sum().sum()
        totais.append(total)
        nomes.append(nome)

    # Criação do gráfico de pizza
    plt.figure(figsize=(10, 8))
    plt.pie(totais, labels=nomes, autopct='%1.1f%%', startangle=140)
    plt.title('Distribuição Percentual dos Focos Ativos por Bioma')
    plt.tight_layout()
    plt.show()

# Chamada para gerar o gráfico de pizza
grafico_pizza_biomas()

def grafico_comparativo(df, bioma_name):
    # Definição dos dados para o gráfico
    anos = df['anos']
    df['total'] = df[
        ['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro',
         'novembro', 'dezembro']].sum(axis=1)

    # Filtra dados até 2023 para calcular máximas, médias e mínimas
    df_historico = df[df['anos'] < '2024']

    # Calcular valores máximos, médios e mínimos mensais
    maximos = df_historico.max()
    medias = df_historico.mean()
    minimos = df_historico.min()

    # Dados do ano corrente (2024)
    ano_corrente = df[df['anos'] == '2024']

    meses = ['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro',
             'novembro', 'dezembro']

    # Criação do gráfico
    plt.figure(figsize=(12, 8))
    plt.plot(meses, maximos[meses], label='Máximos', color='red', linestyle='--')
    plt.plot(meses, medias[meses], label='Médias', color='darkorange', linestyle='-.')
    plt.plot(meses, minimos[meses], label='Mínimos', color='gold', linestyle=':')
    plt.plot(meses, ano_corrente[meses].values[0], label='2024', color='black', marker='o')

    # Configurações do gráfico
    plt.title(f'Comparativo dos Focos Ativos - {bioma_name}')
    plt.xlabel('Meses')
    plt.ylabel('Número de Focos Ativos')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Chamada para gerar o gráfico (exemplo de uso em uma view)
def dashboard_biomas(request):
    filterset = BiomaFilter(request.GET or None)
    bioma_data = None
    bioma_name = None

    if filterset.is_valid():
        bioma_name = filterset.cleaned_data.get('Bioma')
        bioma_model = seletor_bioma(bioma_name)
        if bioma_model:
            bioma_data = obter_dados(bioma_model)
            serie_historica(bioma_data, bioma_name)

    context = {
        'filterset': filterset,
    }
    return render(request, 'dashboard_biomas.html', context)

def heatmap_focos_ativos(df, bioma_name):
    # Preparar os dados para o heatmap
    df_heatmap = df.melt(id_vars=['anos'],
                         value_vars=['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto',
                                     'setembro', 'outubro', 'novembro', 'dezembro'],
                         var_name='mes', value_name='focos_ativos')

    # Criação do heatmap
    plt.figure(figsize=(12, 8))
    heatmap_data = df_heatmap.pivot('anos', 'mes', 'focos_ativos')
    sns.heatmap(heatmap_data, cmap="YlGnBu", annot=True, fmt="g")

    # Configurações do gráfico
    plt.title(f'Heatmap dos Focos Ativos por Mês e Ano - {bioma_name}')
    plt.xlabel('Meses')
    plt.ylabel('Anos')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# Exemplo de chamada para gerar o heatmap para o Bioma selecionado
def visualizar_heatmap(request):
    filterset = BiomaFilter(request.GET or None)
    bioma_data = None
    bioma_name = None

    if filterset.is_valid():
        bioma_name = filterset.cleaned_data.get('Bioma')
        bioma_model = seletor_bioma(bioma_name)
        if bioma_model:
            bioma_data = obter_dados(bioma_model)
            heatmap_focos_ativos(bioma_data, bioma_name)

    context = {
        'filterset': filterset,
    }
    return render(request, 'painel_geral.html', context)
