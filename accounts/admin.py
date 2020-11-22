from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from .models import User
# from django import forms
# from django.contrib.auth.forms import ReadOnlyPasswordHashField


# class RegisterForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ('email','is_staff')

#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         qs = User.objects.filter(email=email)
#         if qs.exists():
#             raise forms.ValidationError("email is taken")
#         return email




# class UserAdminCreationForm(forms.ModelForm):
#     """A form for creating new users. Includes all the required
#     fields, plus a repeated password."""
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ('email', 'is_staff')

#     def clean_password2(self):
#         # Check that the two password entries match
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError("Passwords don't match")
#         return password2

#     def save(self, commit=True):
#         # Save the provided password in hashed format
#         user = super(UserAdminCreationForm, self).save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user


# class UserAdminChangeForm(forms.ModelForm):
#     """A form for updating users. Includes all the fields on
#     the user, but replaces the password field with admin's
#     password hash display field.
#     """
#     password = ReadOnlyPasswordHashField()



#     class Meta:
#         model = User
#         fields = ('is_staff',)


#     class Meta:
#         model = User
#         fields = ('is_staff',)

# class UserAdmin(BaseUserAdmin):
#     # The forms to add and change user instances
#     form = UserAdminChangeForm
#     add_form = UserAdminCreationForm

#     # The fields to be used in displaying the User model.
#     # These override the definitions on the base UserAdmin
#     # that reference specific fields on auth.User.
#     list_display = ('username', 'superuser', 'active', 'staff')
#     list_filter = ('superuser', 'active', 'staff')
#     readonly_fields = [
#         'last_login'
#     ]
#     actions = [
#         'activate_users',
#     ]
#     filter_horizontal = ('user_permissions', 'groups')

#     fieldsets = (
#         (None, {'fields': ('username', 'password', 'config_file')}),
#         ('Permissions', {'fields': ('superuser', 'active', 'staff', 'groups', 'user_permissions')}),
#         ('Important dates', {'fields': ('last_login',)}),
#     )
#     # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
#     # overrides get_fieldsets to use this attribute when creating a user.
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('username', 'password1', 'password2', 'config_file')}
#          ),
#     )
#     search_fields = ('username',)
#     ordering = ('username',)

#     def get_form(self, request, obj=None, **kwargs):
#         form = super().get_form(request, obj, **kwargs)
#         is_superuser = request.user.is_superuser
#         disabled_fields = set()

#         if not is_superuser:
#             disabled_fields |= {
#                 'username',
#                 'active',
#                 'superuser',
#                 'staff',
#                 'groups',
#                 'user_permissions'
#             }
#             if (
#                     not is_superuser
#                     and obj is not None
#                     and obj == request.user
#             ):
#                 disabled_fields |= {
#                     'username',
#                     'active',
#                     'superuser',
#                     'staff',
#                     'groups',
#                     'user_permissions'
#                 }

#             for f in disabled_fields:
#                 if f in form.base_fields:
#                     form.base_fields[f].disabled = True
#         return form

#     def activate_users(self, request, queryset):
#         is_superuser = request.user.is_superuser
#         if is_superuser:
#             cnt = queryset.filter(active=False).update(active=True)
#             self.message_user(request, 'Activated {} users.'.format(cnt))

#     activate_users.short_description = 'Activate Users'

#     def has_add_permission(self, request):
#         return self.request.user.is_admin

#     def has_delete_permission(self, request):
#         return self.request.user.is_admin

#     def has_view_permission(self, request, obj=None):
#         return True

#     def has_change_permission(self, request, obj=None):
#         return True



# admin.site.register(User, UserAdmin)