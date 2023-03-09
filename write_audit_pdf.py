"""Generate a TestMachine Audit PDF given raw data."""
import markdown
from weasyprint import HTML


class AuditPDF:
    """Generate a PDF from raw audit data."""

    markdown_documents = ["ai_report"]

    def __init__(self, audit_data: dict):
        """Assume all raw data is provided in the audit_data dictionary."""
        self.audit_data = audit_data
        self.audit_html = ""
        self.html_sections = {}
        self.translate_markdown()
        self.generate_pdf()

    def translate_markdown(self):
        """Translate the AI-generated markdown documents into HTML for inclusion in report."""
        for doc in self.markdown_documents:
            self.html_sections[doc] = markdown.markdown(self.audit_data[doc])

    def generate_pdf(self):
        """Now that the HTML is fully compiled, let's generate the PDF document."""
        self.audit_html = self.html_sections["ai_report"]
        HTML(string=self.audit_html).write_pdf("audit.pdf")


if __name__ == "__main__":
    # Initialize the audit data.
    audit_data = {}

    # Read in some sample markdown just to test this.
    with open("lib/sample_report.md") as f:
        audit_data["ai_report"] = f.read()

    # Create apdf instance.
    apdf = AuditPDF(audit_data)
