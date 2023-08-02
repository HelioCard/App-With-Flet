from reportlab.platypus import (SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer,
                                Image, PageBreak, HRFlowable)
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import inch, cm
from datetime import datetime

class CustomerReport:
    def __init__(self, filename, data) -> None:  
        self.data = data  
        self.filename = filename
        self.pdf = SimpleDocTemplate(self.filename, pagesize = A4)
        self.table = Table(data)
        self.rowNumb = self.get_rowNumb()

        style = TableStyle([
            ('BACKGROUND', (0,0), (3,0), colors.lightgrey),
            ('TEXTCOLOR',(0,0),(-1,0), colors.black),

            ('ALIGN',(0,0),(-1,-1),'CENTER'),

            ('FONTNAME', (0,0), (-1,0), 'Helvetica'),
            ('FONTSIZE', (0,0), (-1,0), 10),

            ('BOTTOMPADDING', (0,0), (-1,0), 4),

            ('BACKGROUND',(0,1),(-1,-1), colors.white),
        ])
        
        self.table.setStyle(style)

        self.print_report()

    def get_rowNumb(self):
        return len(self.data)
    
    def print_report(self):
        try:
            elems = [self.table]
            self.pdf.build(elems)
            return 'success', None
        except Exception as e:
            return 'error', e


class ProductsReport:
    def __init__(self, filename, data, title) -> None:  
        self.data = data  
        self.filename = filename
        self.pdf = SimpleDocTemplate(self.filename, pagesize = A4)
        self.table = Table(data)        
        self.title = title
        self.paragraph_style = ParagraphStyle(name='Centered', alignment=TA_CENTER, fontSize=14, leading=16)
        self.table_style = TableStyle([
            ('BACKGROUND', (0,0), (4,0), colors.lightgrey),
            ('TEXTCOLOR',(0,0),(-1,0), colors.black),

            ('ALIGN',(0,0),(-1,-1),'CENTER'),

            ('FONTNAME', (0,0), (-1,0), 'Helvetica'),
            ('FONTSIZE', (0,0), (-1,0), 10),

            ('BOTTOMPADDING', (0,0), (-1,0), 4),

            ('BACKGROUND',(0,1),(-1,-1), colors.white),
        ])

    def get_date_time(self):
        now = datetime.now()
        date = now.strftime("%d/%m/%Y")
        time = now.strftime("%H:%M:%S")
        return f"({date} - {time})"
    
    def print_report(self):
        try:
            story = [Paragraph(self.title, self.paragraph_style)]            
            story.append(Paragraph(self.get_date_time(), self.paragraph_style))
            story.append(Spacer(1, 0.5 * inch))
            
            self.table.setStyle(self.table_style)
            story.append(self.table)
            
            self.pdf.build(story)
            return 'success', self.filename
        except Exception as e:
            return 'error', e
        

class SaleReport:
    # filename

    # header_data = [
    #     'Empresa XYZ',
    #     'Rua ABC, 123',
    #     '(99) 9999-9999',
    #     'empresa@xyz.com'
    # ]

    # sale_data = [
    #     '001',
    #     '26/06/2023'
    # ]

    # customer_data = [
    #     'Cliente A',
    #     '123.456.789-00',
    #     '(88) 8888-8888',
    #     'cliente@cliente.com',
    #     'Rua Cliente, 456'
    # ]

    # products_data = [[], [], [], ...] list of lists

    def __init__(self, filename, header_data, sale_data, customer_data, products_data) -> None:
        self.filename = filename
        self.header_data = header_data
        self.sale_data = sale_data
        self.customer_data = customer_data
        self.products_data = products_data
        self.pdf = None
        self.numb_pages = int

    def get_header_data(self):
        # Cabeçalho com o logo e os dados da empresa
        logo = Image("C:\logo.png", 50, 50)

        header_table = Table([
            [logo, "", self.header_data[0]], 
            ["", "", self.header_data[1]],
            ["", "", f"{self.header_data[2]} - {self.header_data[3]}"]
        ])
        
        header_table.setStyle(TableStyle([
            ('FONTNAME', (2, 0), (2, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (2, 0), (2, 0), 14),
            ('FONTNAME', (2, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (2, 1), (-1, -1), 12),
            ('LEFTPADDING', (0, 0), (-1, -1), 0),
            ('TOPPADDING', (0, 0), (-1, -1), 0),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
            ('SPAN',(0,0),(1,2)),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')
        ]))
        
        return header_table

    def get_sale_data(self):
        # Número do pedido e data
        sale_table = Table([[f"Pedido número: {self.sale_data[0]} - Data: {self.sale_data[1]}"]])
        sale_table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 13),
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.black)
        ]))
        return sale_table

    def get_customer_data(self):
        # Dados do cliente
        customer_table = Table([
            [f"Cliente: {self.customer_data[0]} - CPF: {self.customer_data[1]}"],
            [f"Tel.: {self.customer_data[2]} - E-mail: {self.customer_data[3]}"],
            [self.customer_data[4]]
        ])
        customer_table.setStyle(TableStyle([
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 12),
            ('LEFTPADDING', (0, 0), (-1, -1), 0),
            ('TOPPADDING', (0, 0), (-1, -1), 0),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')
        ]))
        return customer_table

    def get_products_table_data(self, products_data):
        # Dados dos produtos
        products_table = []
        products_table.append(['CÓD. PROD.', 'DESCRIÇÃO', 'MARCA', 'QUANT', 'V. UNIT.', 'V. Total'])

        for products in products_data:
            products_table.append(products)
        table = Table(products_table)
        
        style = TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 9),
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
            ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ])
        if products_data[-1][4] == "Total:":
            style.add('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold')
            style.add('BACKGROUND', (0, -1), (-1, -1), colors.lightgrey)

        table.setStyle(style)
        return table

    def draw_footer(self, canvas, doc):
        canvas.saveState()
        canvas.setFont("Helvetica", 8)
        canvas.drawRightString(A4[0]-cm, cm, "Página %d de %d" % (doc.page, self.numb_pages))
        canvas.restoreState()
        
    def create_pdf(self):
        try:
            self.pdf = SimpleDocTemplate(self.filename, pagesize=A4, leftMargin=1*cm, rightMargin=1*cm, topMargin=1*cm, bottomMargin=1*cm)

            story = []
            max_items_per_page = 25
            num_items = len(self.products_data)
            self.numb_pages = num_items // max_items_per_page + (num_items % max_items_per_page > 0)

            line = HRFlowable(width="100%", thickness=1, lineCap='round', color=colors.black)
            dotted_line = HRFlowable(width="100%", thickness=1, lineCap='round', color=colors.black, dash=(2, 2))

            for page in range(self.numb_pages):
                story.extend(
                    (
                        line,
                        Spacer(1, 0.5 * cm),
                        self.get_header_data(),
                        Spacer(1, 0.5 * cm),
                        line,
                        Spacer(1, 0.5 * cm),
                        self.get_sale_data(),
                        self.get_customer_data(),
                        Spacer(1, 0.5 * cm),
                    )
                )

                inicio = page * max_items_per_page
                fim = min((page + 1) * max_items_per_page, num_items)
                story.append(self.get_products_table_data(self.products_data[inicio:fim]))

                if page < self.numb_pages - 1:
                    story.extend((Spacer(1, 0.5 * cm), dotted_line, PageBreak()))

            story.extend((Spacer(1, 0.5 * cm), line))
            self.pdf.build(story, onFirstPage=self.draw_footer, onLaterPages=self.draw_footer)
            return "success", None
        except Exception as e:
            return "error", e
    