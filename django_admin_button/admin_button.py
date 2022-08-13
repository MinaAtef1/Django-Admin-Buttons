from django.utils.html import format_html


class AdminActionButton():
    def __init__(self, id, action_name, disabled = False, Class='btn-primary', label=None):
        self.id = id
        self.action_name = action_name
        self.disabled = "disabled" if disabled else ""
        self.Class = Class
        self.label = label or action_name

    def render(self):

        return format_html(f"""
        <div class="bootstrap" style="width:fit-content">
                <button {self.disabled} type="button" onclick="button_action('{self.id}','{self.action_name}')" class="btn btn-sm {self.Class}">{self.label}</button>
        </div>
        """)