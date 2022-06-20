from django.shortcuts import render

def profile(request):
    """View to display the profile of the currently
    logged-in user.
    """

    return render(request, 'accounts/profile.html')
