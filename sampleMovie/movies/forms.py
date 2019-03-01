from django import forms
from movies.models import Persona, Plan, TipoPlan, Peliculas, Log, RatingPeliculas

class PlanForm(forms.ModelForm):
	class Meta:
		fields = [
			'tipo',
		]
		labels = {
			'tipo':'Tipo',
			}
		widgets = {
			'plan':forms.Select(),
		}

class TipoPlanForm(forms.ModelForm):
	class Meta:
		fields = [
			'nombre',
			'costo',
		]
		labels = {
			'nombre':'Nombre',
			'costo':'Costo',
			}
		widgets = {
			'nombre':forms.TextInput(),
			'costo':forms.TextInput(),
		}

class PersonaForm(forms.ModelForm):
	class Meta:
		fields = [
			'nombre',
			'apellido',
			'fecha',
			'plan',
		]
		labels = {
			'nombre':'Nombre',
			'apellido':'Apellido',
			'fecha':'Fecha',
			'plan':'Plan',
			}
		widgets = {
			'nombre':forms.TextInput(),
			'apellido':forms.TextInput(),
			'fecha':forms.TextInput(),
			'plan':forms.Select(),
		}

class RatingForm(forms.ModelForm):
	class Meta:
		model = RatingPeliculas
		fields=[
			'pelicula',
			'persona',
			'cali',
		]

		labels={
			'persona':'Usuarios',
			'pelicula':'Peliculas',
			'cali':'Calificacion',		
			}
		widgets = {
			'persona':forms.Select(attrs={'class':'form-control'}),
			'pelicula':forms.Select(attrs={'class':'form-control'}),
			'cali':forms.TextInput(attrs={'class':'form-control'})
		}

