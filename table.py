from docxtpl import DocxTemplate
from pathlib import Path

document_path = Path(__file__).parent / "example_document.docx"
doc = DocxTemplate(document_path)

invoices = [
    ["21-2-2024", "Speech pathology services - 60 mins - school visit", "15_005_0118_1_3", "193.99"],
    ["21-2-2024", "Speech pathology services - 15 mins - provider travel to Penshurst West", "15_005_0118_1_3", "48.50"],
    ["28-2-2024", "Speech pathology services - 60 mins - school visit", "15_005_0118_1_3", "193.99"],
    ["28-2-2024", "Speech pathology services - 15 mins - provider travel to Penshurst West", "15_005_0118_1_3", "48.50"],
]

context = {
    "name": "Tommo",
    "invoices": invoices,
}


doc.render(context)
doc.save(Path(__file__).parent / "new_document.docx")
