from django import forms

class ContactForm(forms.Form):
    senderName = forms.CharField(
        max_length = 255, 
        label = "Your Name",
        help_text = "Optional, but I'd love to know what your name is!",
        required = False
        )
    senderEmail = forms.EmailField(
        max_length = 255,
        label = "email Address",
        help_text = "Again, optional, but I'd love to be able to respond to you! Don't worry, I won't add you to any mailing lists.",
        required = False
    )
    senderMessage = forms.CharField(
        widget = forms.Textarea,
        label = "What Do You Want To Say?",
        required = True
    )