from django.contrib import admin
from .models import Company

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name',)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Employee
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

# Form to add new employees
class EmployeeCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = Employee
        fields = ('employee_id', 'name')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

# Form to update employee
class EmployeeChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Employee
        fields = ('employee_id', 'name', 'password', 'is_active')

    def clean_password(self):
        return self.initial["password"]

# Custom admin
class EmployeeAdmin(BaseUserAdmin):
    form = EmployeeChangeForm
    add_form = EmployeeCreationForm

    list_display = ('employee_id', 'name', 'is_active')
    list_filter = ('is_active',)
    fieldsets = (
        (None, {'fields': ('employee_id', 'password')}),
        ('Personal Info', {'fields': ('name',)}),
        ('Permissions', {'fields': ('is_active',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('employee_id', 'name', 'password1', 'password2', 'is_active')}
        ),
    )
    search_fields = ('employee_id', 'name')
    ordering = ('employee_id',)
    filter_horizontal = ()

admin.site.register(Employee, EmployeeAdmin)

