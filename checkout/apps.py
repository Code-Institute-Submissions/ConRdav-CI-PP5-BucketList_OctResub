from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """ Checkout config """
    name = 'checkout'

    def ready(self):
        """ checkout signal """
        import checkout.signals
