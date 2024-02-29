import sentry_sdk.transport as transport


class DEFAULT_HTTP_TRANSPORT(transport.HttpTransport):
    def _get_pool_options(self, ca_certs):
        # Ignore SSL Errors
        options = super()._get_pool_options(ca_certs)
        options["cert_reqs"] = "CERT_NONE"
        return options
