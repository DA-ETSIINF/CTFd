from CTFd.plugins import register_plugin_assets_directory
from CTFd.plugins.flags import FLAG_CLASSES, BaseFlag
from CTFd.utils.user import get_current_user
import hashlib


# Represents a flag about
class TryITFlag(BaseFlag):
    name = "TryIT"
    templates = {  # Nunjucks templates used for key editing & viewing
        "create": "/plugins/daetsiinf_tryit_flag/assets/create.html",
        "update": "/plugins/daetsiinf_tryit_flag/assets/edit.html",
    }


    @staticmethod
    def compare(chal_key_obj, provided):
        saved = chal_key_obj.content

        expected_flag_content = "%d:%s" % (get_current_user().id, saved)
        expected_input = "tryIT{%s}" % hashlib.md5(expected_flag_content.encode('utf-8')).hexdigest()
        return expected_input == provided


def load(app):
    FLAG_CLASSES["TryIT"] = TryITFlag
    register_plugin_assets_directory(app, base_path="/plugins/daetsiinf_tryit_flag/assets/")
