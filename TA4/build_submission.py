"""Build the standalone Python program and PDF submission from the TA4 notebook."""

import json
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import PageBreak, Paragraph, Preformatted, SimpleDocTemplate, Spacer


ROOT = Path(__file__).resolve().parent
NOTEBOOK = ROOT / "trading_assistant.ipynb"
PYTHON_OUTPUT = ROOT / "trading_assistant.py"
PDF_OUTPUT = ROOT / "TA4_Ibasco.pdf"


def extract_output(code_cell):
    parts = []
    for output in code_cell.get("outputs", []):
        if output.get("output_type") == "stream":
            text = output.get("text", "")
            parts.append("".join(text) if isinstance(text, list) else text)
        elif output.get("output_type") == "error":
            parts.append("\n".join(output.get("traceback", [])))
        else:
            text = output.get("data", {}).get("text/plain", "")
            parts.append("".join(text) if isinstance(text, list) else text)
    return "\n".join(part.rstrip() for part in parts if part).strip()


def draw_footer(canvas, document):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#555555"))
    canvas.drawString(0.7 * inch, 0.42 * inch, "CS0065 Technical Assessment 4")
    canvas.drawRightString(7.8 * inch, 0.42 * inch, f"Page {document.page}")
    canvas.restoreState()


def build():
    notebook = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
    code_cell = notebook["cells"][-1]
    if code_cell.get("cell_type") != "code":
        raise ValueError("The notebook must end with the complete program.")

    code = "".join(code_cell.get("source", []))
    output = extract_output(code_cell)
    PYTHON_OUTPUT.write_text(code.rstrip() + "\n", encoding="utf-8")

    pdfmetrics.registerFont(TTFont("NotoSansMono", "/usr/share/fonts/noto/NotoSansMono-Light.ttf"))
    base = getSampleStyleSheet()
    title = ParagraphStyle(
        "Title", parent=base["Title"], alignment=TA_CENTER, fontName="Helvetica-Bold",
        fontSize=20, leading=24, textColor=colors.black, spaceAfter=14,
    )
    subtitle = ParagraphStyle(
        "Subtitle", parent=base["Normal"], alignment=TA_CENTER, fontSize=11,
        leading=15, spaceAfter=6,
    )
    heading = ParagraphStyle(
        "Heading", parent=base["Heading1"], fontName="Helvetica-Bold",
        fontSize=14, leading=18, textColor=colors.black, spaceBefore=10, spaceAfter=7,
    )
    body = ParagraphStyle(
        "Body", parent=base["BodyText"], fontName="Helvetica", fontSize=10.5,
        leading=15, spaceAfter=8,
    )
    code_style = ParagraphStyle(
        "Code", fontName="NotoSansMono", fontSize=6.5, leading=8.3,
        leftIndent=4, rightIndent=4, textColor=colors.HexColor("#202020"),
        backColor=colors.HexColor("#F4F4F4"), borderColor=colors.HexColor("#D9D9D9"),
        borderWidth=0.5, borderPadding=7, spaceAfter=10,
    )
    output_style = ParagraphStyle(
        "Output", parent=code_style, fontSize=7.3, leading=9.3,
        backColor=colors.HexColor("#F8FAFC"),
    )

    document = SimpleDocTemplate(
        str(PDF_OUTPUT), pagesize=letter, rightMargin=0.7 * inch, leftMargin=0.7 * inch,
        topMargin=0.65 * inch, bottomMargin=0.65 * inch,
        title="Beginner Trading Assistant Using RBR and CBR", author="Ezekiel M. Ibasco",
    )

    story = [
        Paragraph("Beginner Trading Assistant Using RBR and CBR", title),
        Paragraph("Knowledge Representation and Reasoning", subtitle),
        Paragraph("Ezekiel M. Ibasco | AN42", subtitle),
        Spacer(1, 12),
        Paragraph("Knowledge Base and Use Case", heading),
        Paragraph(
            "The knowledge base uses three categories: market, investor, and portfolio. Its facts include "
            "price, moving average, RSI, trend, volatility, risk tolerance, experience, emergency-fund "
            "status, ownership, allocation, and available cash. The use case is a beginner seeking a simple "
            "educational interpretation of a manually entered market snapshot. The assistant does not access "
            "live prices, execute trades, or provide financial advice.", body,
        ),
        Paragraph("Rule Based Reasoning", heading),
        Paragraph(
            "Six IF-THEN functions examine trend confirmation, RSI, volatility and risk compatibility, "
            "portfolio concentration, available cash and emergency savings, and beginner position sizing. "
            "The inference engine checks every rule and prints every applicable action.", body,
        ),
        Paragraph("Case Based Reasoning", heading),
        Paragraph(
            "Four past cases contain problem features and solutions. Retrieval uses weighted exact matching: "
            "trend 30 percent, RSI band 25 percent, volatility 20 percent, risk tolerance 15 percent, and "
            "experience 10 percent. The system reuses the closest solution, permits manual revision, and "
            "retains the new case.", body,
        ),
        Paragraph("Comparative Reflection", heading),
        Paragraph(
            "RBR was easier to implement because each condition and action could be written directly as an "
            "IF-THEN rule. CBR is more flexible for unstructured problems because it can reuse experience even "
            "without an exact match. CBR can adapt more naturally to continuously changing data, although its "
            "case base must be reviewed. RBR fits compliance checks, eligibility screening, and safety alerts. "
            "CBR fits troubleshooting, support, case review, and recommendations. Here, RBR explains triggered "
            "limits clearly, while CBR suggests an action from the most similar past market situation.", body,
        ),
        PageBreak(),
        Paragraph("Complete Python Program", heading),
        Preformatted(code, code_style, maxLineLength=104),
        Spacer(1, 12),
        Paragraph("Program Output", heading),
        Preformatted(output, output_style, maxLineLength=96),
    ]
    document.build(story, onFirstPage=draw_footer, onLaterPages=draw_footer)
    print(f"Created {PYTHON_OUTPUT}")
    print(f"Created {PDF_OUTPUT}")


if __name__ == "__main__":
    build()
