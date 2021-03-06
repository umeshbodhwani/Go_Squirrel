from django.db import models
from django.utils.translation import gettext as _
# Create your models here.
class Squirrel(models.Model):
    
    AM = 'AM'
    PM = 'PM'

    ADULT = 'ADULT'
    JUVENILE = 'JUVENILE'
    
    Gray = 'GRAY'
    Cinnamon = 'CINAMMON'
    Black = 'BLACK'
    
    AGE_CHOICES = (
            (ADULT, 'ADULT'),
            (JUVENILE, 'JUVENILE'),)
    
    TIME_DAY = (
            (AM, 'AM'),
            (PM, 'PM'),
        )
    
    FUR_COLOR = (
            (Gray, 'GRAY'),
            (Cinnamon, 'CINNAMON'),
            (Black, 'BLACK'))
    
    GROUND_PLANE = 'GROUND PLANE'
    ABOVE_GROUND = 'ABOVE GROUND'
    
    LOCATION= (
            (GROUND_PLANE, 'GROUND PlANE'),
            (ABOVE_GROUND, 'ABOVE GROUND'),)
    
    X = models.DecimalField(
            help_text = _('Longitude'),
            max_digits = 20,
            blank = True,
            decimal_places = 15,
            )

    Y = models.DecimalField(
            help_text = _('Latitude'),
            max_digits = 20,
            blank = True,
            decimal_places = 15,)

    Unique_squirrel_ID = models.CharField(
            help_text=_('Hectare + Shift + Date + Hectare squirrel number'),
            primary_key = True,
            max_length=20,)

    Shift = models.CharField(
            help_text=_('AM or PM'),
            choices = TIME_DAY,
            blank = True,
            max_length=20,
        )

    Date = models.IntegerField(
            help_text=_('Date when squirrel was spotted'),
            blank = True,
            null = True,)

    Age = models.CharField(
            help_text=_('Adult or Juvenile'),
            choices = AGE_CHOICES,
            blank = True,
            max_length=20,
        )

    Primary_Fur_Color = models.CharField(
            help_text=_('gray, cinnamon or black'),
            choices = FUR_COLOR,
            blank = True,
            max_length=20,)

    Location = models.CharField(
            help_text=_('Ground plane or above ground'),
            choices = LOCATION,
            blank = True,
            max_length=20,)

    Specific_Location = models.CharField(
            help_text=_('Comments on the squirrel location'),
            blank = True,
            max_length=20,)

    Running = models.BooleanField(
            help_text=_('True if squirrel was running'),
            default=False,)

    Chasing = models.BooleanField(
            help_text=_('True if squirrel was chasing'),
            default=False,)

    Climbing = models.BooleanField(
            help_text=_('True if squirrel was climbing'),
            default=False,)

    Eating = models.BooleanField(
            help_text=_('True if squirrel was eating'),
            default=False,)

    Foraging = models.BooleanField(
            help_text=_('True if squirrel was foraging'),
            default=False,)

    Other_Activities = models.CharField(
            help_text=_('Other activity by squirrel'),
            max_length=20,
            blank=True,)

    Kuks = models.BooleanField(
            help_text=_('Is  Squirrel kuking'),
            default=False,
        )

    Quaas = models.BooleanField(
            help_text=_('Is  Squirrel quaaing'),
            default=False,
        )

    Moans = models.BooleanField(
            help_text=_('Is Squirrel Moaning'),
            default=False,
        )

    Tail_flags = models.BooleanField(
            help_text=_('Is Squirrel flagging tail'),
            default=False,
        )

    Tail_twitching = models.BooleanField(
            help_text=_('Is the Squirrel twitching tail'),
            default=False,
        )

    Approaches = models.BooleanField(
        help_text=_('Is Squirrel approaching human'),
        default=False,
        )

    Indifferent = models.BooleanField(
            help_text=_('Is squirrel indifferent to human'),
        default=False,
        )
    Runs_from = models.BooleanField(
            help_text=_('Is Squirrel running from human'),
            default=False,
        )

    def __str__(self):
        return self.Unique_squirrel_ID


