
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import FormView
from django.utils.decorators import method_decorator
from invitations.utils import get_invitation_model, get_invite_form

Invitation = get_invitation_model()
InviteForm = get_invite_form()

# Overrides 'SendInvite class in django-invatations'
class SendInvite(FormView):
    template_name = "invitations/forms/_invite.html"
    form_class = InviteForm

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(SendInvite, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        email = form.cleaned_data["email"]

        try:
            invite = form.save(email)
            invite.inviter = self.request.user
            invite.save()
            invite.send_invitation(self.request)
        except Exception:
            return self.form_invalid(form)
        return self.render_to_response(
            self.get_context_data(
                success_message=("%(email)s has been invited") % {"email": email}
            )
        )

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
