import os
import random
import argparse

try:
    from faker import Faker
except ImportError:
    print("ERRORE: La libreria 'Faker' non è installata.")
    print("Per favore esegui 'pip install faker' prima di lanciare lo script.")
    exit(1)

fake = Faker('it_IT')

# Vocabolario ERP simulato per rendere le frasi coerenti col dominio
ERP_MODULES = ["Magazzino", "Contabilità", "Fatturazione", "Risorse Umane", "Produzione", "Logistica", "Acquisti", "Vendite"]
ERP_ISSUES = ["Errore 500", "Timeout Database", "Credenziali non valide", "Crash applicativo", "Spazio su disco esaurito", "Connessione rifiutata", "VPN disconnessa"]

def generate_how_to(file_path):
    module = random.choice(ERP_MODULES)
    title = f"Come configurare il modulo {module}: {fake.catch_phrase()}"
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(f"# {title}\n\n")
        
        f.write("## Panoramica\n")
        f.write(f"Questa procedura illustra i passaggi per la corretta configurazione di {module}. {fake.paragraph(nb_sentences=3)}\n\n")
        
        f.write("## Prerequisiti\n")
        for _ in range(random.randint(2, 4)):
            f.write(f"- {fake.sentence()}\n")
        f.write("\n")
        
        f.write("## Procedura\n")
        f.write(f"Assicurarsi di seguire le istruzioni nell'ordine corretto per il modulo {module}.\n")
        for i in range(1, random.randint(4, 9)):
            f.write(f"{(i)}. {fake.sentence()}\n")
        f.write("\n")
        
        f.write("## Verifiche finali\n")
        f.write(f"{fake.paragraph(nb_sentences=2)}\n")

def generate_troubleshooting(file_path):
    module = random.choice(ERP_MODULES)
    issue = random.choice(ERP_ISSUES)
    title = f"Risoluzione problema {issue} in {module}"
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(f"# {title}\n\n")
        
        f.write("## Sintomo\n")
        f.write(f"L'utente riscontra il seguente comportamento anomalo: {fake.paragraph(nb_sentences=3)}\n\n")
        
        f.write("## Cause probabili\n")
        for _ in range(random.randint(2, 4)):
            f.write(f"- {fake.sentence()}\n")
        f.write("\n")
        
        f.write("## Risoluzione\n")
        f.write("Applicare la seguente sequenza di ripristino:\n")
        for i in range(1, random.randint(3, 6)):
            f.write(f"{(i)}. {fake.sentence()}\n")
        f.write("\n")
        
        f.write("## Quando escalare\n")
        f.write(f"Se l'errore persiste dopo la risoluzione: {fake.sentence()}\n")

def generate_reference(file_path):
    module = random.choice(ERP_MODULES)
    title = f"Riferimento Tecnico: Tabelle e Regole di {module}"
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(f"# {title}\n\n")
        
        f.write("Queste sono le specifiche tecniche per le entità di dominio.\n\n")
        
        f.write("## Campi\n")
        for _ in range(random.randint(2, 4)):
            field_name = fake.word().capitalize()
            f.write(f"### {field_name}\n")
            f.write(f"**Tipo:** {random.choice(['String', 'Integer', 'Boolean', 'Date', 'Float'])}\n")
            f.write(f"**Descrizione:** {fake.sentence()}\n\n")
        
        f.write("## Regole\n")
        for _ in range(random.randint(2, 4)):
            rule_name = f"Regola {fake.word().capitalize()}"
            f.write(f"### {rule_name}\n")
            f.write(f"**Condizione:** {fake.sentence()}\n")
            f.write(f"**Validazione:** {fake.paragraph(nb_sentences=2)}\n\n")

def main():
    parser = argparse.ArgumentParser(description="Generate synthetic Markdown knowledge base files.")
    parser.add_argument("--count", type=int, default=50, help="Number of files to generate (default: 50)")
    parser.add_argument("--outdir", type=str, default="mock_knowledge_base", help="Output directory (default: mock_knowledge_base)")
    args = parser.parse_args()

    os.makedirs(args.outdir, exist_ok=True)
    
    generators = [
        ("howto", generate_how_to),
        ("ts", generate_troubleshooting),
        ("ref", generate_reference)
    ]
    
    print(f"Generating {args.count} mock documents in '{args.outdir}'...")
    
    for i in range(args.count):
        prefix, generator_func = random.choice(generators)
        filename = f"{prefix}_{fake.uuid4()[:8]}.md"
        file_path = os.path.join(args.outdir, filename)
        generator_func(file_path)
        
    print(f"✅ Fatto! Generati {args.count} file in {args.outdir}")

if __name__ == "__main__":
    main()
