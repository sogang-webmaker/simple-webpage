from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
	author = models.ForeignKey('auth.User')
	#for many to one model
	#왜냐하면 여러 글이 한 사용자 로부터 나오기 때문
	title = models.CharField(max_length=150)
	text = models.TextField()
	start_time = models.DateTimeField(default = timezone.now)

	end_time = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.end_time = timezone.now()
		self.save()

	def __str__(self):
		return self.title

	#제목을 반환한다. 

#게시글 포스트롤 완성했다. 



