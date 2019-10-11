{
    'name': 'Mi Libreria',
    'summary': 'Manejo de libros de forma sencilla',
    'description': '''Descripción muy larga''',
    'author': 'Diego Vásquez Cornejo',
    'website': 'www.apps.odoo.com',
    'category': 'Sin Categoria',
    'version': '12.0.1',
    'depends': ['base'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/library_book.xml'
    ],
    # 'demo': ['demo.xml'],
    'application': True,
    'installable': True
}