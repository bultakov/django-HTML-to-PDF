from io import BytesIO

from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf.document import pisaDocument


def html_to_pdf(template_src: str, context: dict = {}):
    template = get_template(template_src)
    html = template.render(context)
    result = BytesIO()
    pdf: pisaDocument = pisaDocument(BytesIO(html.encode("UTF-8")), result, encoding='UTF-8')
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None
