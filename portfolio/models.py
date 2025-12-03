from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100, default="")
    message = models.CharField(max_length = 500)
    date = models.DateField()
    
    
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Project(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    image = models.ImageField(upload_to='projects/')
    github = models.URLField(blank=True, null=True)
    demo = models.URLField(blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
            


class Skill(models.Model):
    LEVEL_CHOICES = [
        ("Beginner", "Beginner"),
        ("Intermediate", "Intermediate"),
        ("Intermediate+", "Intermediate+"),
        ("Good", "Good"),
        ("Advanced", "Advanced"),
        ("Growing", "Growing"),
        ("Comfortable", "Comfortable"),
    ]

    title = models.CharField(max_length=200)
    level = models.CharField(max_length=50, choices=LEVEL_CHOICES)
    percentage = models.PositiveIntegerField(default=50)

    # Tags like HTML, CSS, Pandas...
    tags = models.TextField(help_text="Comma-separated values")  

    def tag_list(self):
        return [tag.strip() for tag in self.tags.split(",")]

    def __str__(self):
        return self.title
        
class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="projects/gallery/")

    def __str__(self):
        return f"Image of {self.project.title}"        