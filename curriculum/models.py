from django.db import models

class Checkpoint(models.Model):
    """
    Represents a static position or checkpoint in a technique.
    Examples: Guard, Side Control, Mount, Full Mount, Half Guard, etc.
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Technique(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    init_checkpoint = models.ForeignKey(
        Checkpoint, 
        on_delete=models.SET_NULL, 
        related_name='techniques_starting_from', 
        null=True, 
        blank=True
    )
    out_checkpoint = models.ForeignKey(
        Checkpoint, 
        on_delete=models.SET_NULL, 
        related_name='techniques_ending_at', 
        null=True, 
        blank=True
    )
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='techniques')
    belt_level = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return self.name

class KeyPoint(models.Model):
    technique = models.ForeignKey(Technique, on_delete=models.CASCADE, related_name='key_points')
    description = models.CharField(max_length=255)
    
    def __str__(self):
        return self.description

class CommonMistake(models.Model):
    technique = models.ForeignKey(Technique, on_delete=models.CASCADE, related_name='common_mistakes')
    description = models.CharField(max_length=255)
    
    def __str__(self):
        return self.description