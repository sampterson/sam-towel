from django.db import models

# Create your models here.
class RiderModel(models.Model):
    """A model to contain stats for each member of Snake Trip"""

    # Fields
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    nickName = models.CharField(max_length=30)
    sport = models.CharField(max_length=15) # TODO: make an enum?

    
    # Metadata
    # class Meta:
    #     ordering = ['-turnNumber']

    # Methods
    # def get_absolute_url(self):
    #     """Returns the url to access a particular instance of MyModelName."""
    #     return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.nickName + '( ' + self.firstName + ' ' + self.lastName + ' )'
