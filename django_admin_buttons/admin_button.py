from django.utils.html import format_html


class AdminActionButton():
    def __init__(self, id, action_name=None, url=None, disabled="", Class='btn-primary', label=None, confirm=True):
        self.id = id
        self.action_name = action_name
        self.url = url
        self.disabled = disabled
        self.Class = Class
        self.label = label
        self.confirm = confirm

    def render(self):
        if self.url:
            confirm = "return confirm('Are you sure you want to perform this action?')" if self.confirm else ""
            return format_html(f"""
            <div class="bootstrap-5" style="width:fit-content;margin-top:1px;margin-bottom:1px">
                <a {self.disabled} href="{self.url}" class="btn btn-sm {self.Class}"
                {confirm}>{self.label}</a>
            </div>
        """)
        else:
            return format_html(f"""
                <div class="bootstrap-5" style="width:fit-content;margin-top:1px;margin-bottom:1px">
                    <button {self.disabled} type="button" onclick="button_action('{self.id}','{self.action_name}')" class="btn btn-sm {self.Class}">{self.label or self.action_name}</button>
                </div>
            """)


class AdminActionButtonGrouping():
    def __init__(self, list):
        self.list = list

    def render(self):
        html = ''
        for action in self.list:
            html += action.render()
        return format_html(html)
