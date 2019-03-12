from django.db import models

# Create your models here.
class Course(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=500)
	number_of_semesters = models.IntegerField()
	current_semester = models.IntegerField()
	age_group = models.ForeignKey('AgeGroup', null=True, on_delete=models.SET_NULL)

	class Meta:
		verbose_name = "Kurs"
		verbose_name_plural = "Kursy"

	def __str__(self):
		return self.name + ( (" sem " + str(self.current_semester)) if self.number_of_semesters > 1 else "")

class Lesson(models.Model):
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=200)
	course = models.ForeignKey('Course', on_delete=models.CASCADE)
	lesson_number = models.IntegerField()

	class Meta:
		verbose_name = "Lekcja"
		verbose_name_plural = "Lekcje"

	def __str__(self):
		return self.name


class Exercise(models.Model):
	exercise_number = models.IntegerField()
	description = models.CharField(max_length=500)
	points = models.IntegerField()
	lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE)

	class Meta:
		verbose_name = "Ćwiczenie"
		verbose_name_plural = "Ćwiczenia"

	def __str__(self):
		return str(self.lesson) + " - Ex. " + str(self.exercise_number)


class AgeGroup(models.Model):
	name = models.CharField(max_length=30)

	class Meta:
		verbose_name = "Grupa wiekowa"
		verbose_name_plural = "Grupy wiekowe"

	def __str__(self):
		return self.name
    