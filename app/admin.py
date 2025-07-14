from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import Company, Employee

# --- Company Admin ---
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name',)

# --- Employee Creation Form ---
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

# --- Employee Update Form ---
class EmployeeChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(label="Password", help_text="Raw passwords are not stored, so there is no way to see this user’s password.")

    class Meta:
        model = Employee
        fields = ('employee_id', 'name', 'password', 'is_active', 'is_staff', 'profile_picture')

    def clean_password(self):
        return self.initial["password"]

# --- Employee Admin ---
class EmployeeAdmin(BaseUserAdmin):
    form = EmployeeChangeForm
    add_form = EmployeeCreationForm

    list_display = ('employee_id', 'name', 'is_active', 'is_staff')
    list_filter = ('is_active', 'is_staff')

    fieldsets = (
        (None, {'fields': ('employee_id', 'password')}),
        ('Personal Info', {'fields': ('name', 'profile_picture')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('employee_id', 'name', 'password1', 'password2', 'is_active', 'is_staff')}
        ),
    )

    search_fields = ('employee_id', 'name')
    ordering = ('employee_id',)
    filter_horizontal = ('groups', 'user_permissions')

# --- Register Employee ---
admin.site.register(Employee, EmployeeAdmin)
