from django.db import models
from common.models import User
from accounts.models import Account
from contacts.models import Contact
from django.utils.translation import ugettext_lazy as _


class Task(models.Model):

    STATUS_CHOICES = (
        ("New", "New"),
        ("In Progress", "In Progress"),
        ("Completed", "Completed")
    )

    PRIORITY_CHOICES = (
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High", "High")
    )

    title = models.CharField(_("title"), max_length=200)
    status = models.CharField(
        _("status"), max_length=50, choices=STATUS_CHOICES)
    priority = models.CharField(
        _("priority"), max_length=50, choices=PRIORITY_CHOICES)
    due_date = models.DateField(blank=True, null=True)

    account = models.ForeignKey(
        Account, related_name='accounts_tasks', null=True, blank=True, on_delete=models.SET_NULL)

    contacts = models.ManyToManyField(
        Contact, related_name="contacts_tasks")

    assigned_to = models.ManyToManyField(
        User, related_name='users_tasks')

    created_by = models.ForeignKey(
        User, related_name='task_created', blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-due_date']
