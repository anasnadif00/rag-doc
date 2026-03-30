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

def generate_yaml_front_matter(title, doc_kind, domain, feature):
    return f"""---
title: "{title}"
doc_kind: "{doc_kind}"
domain: "{domain}"
feature: "{feature}"
keywords: ["erp", "mock", "test"]
task_tags: ["synthetic"]
erp_versions: ["v1.0"]
role_scope: ["all"]
review_status: "approved"
---
"""

def generate_how_to(file_path, domain, feature):
    title = f"Come configurare {feature} in {domain}"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(generate_yaml_front_matter(title, "how_to", domain, feature))
        f.write(f"# {title}\n\n")
        f.write("## Panoramica\n")
        f.write(f"Questa procedura illustra i passaggi d'uso. {fake.paragraph(nb_sentences=3)}\n\n")
        f.write("## Prerequisiti\n")
        for _ in range(random.randint(2, 4)):
            f.write(f"- {fake.sentence()}\n")
        f.write("\n")
        f.write("## Procedura\n")
        f.write(f"Istruzioni operative per {feature}.\n")
        for i in range(1, random.randint(4, 9)):
            f.write(f"{(i)}. {fake.sentence()}\n")
        f.write("\n")
        f.write("## Verifiche finali\n")
        f.write(f"{fake.paragraph(nb_sentences=2)}\n")

def generate_troubleshooting(file_path, domain, feature):
    issue = random.choice(ERP_ISSUES)
    title = f"Risoluzione problema {issue} in {feature}"
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(generate_yaml_front_matter(title, "troubleshooting", domain, feature))
        f.write(f"# {title}\n\n")
        f.write("## Sintomo\n")
        f.write(f"Comportamento anomalo: {fake.paragraph(nb_sentences=3)}\n\n")
        f.write("## Cause probabili\n")
        for _ in range(random.randint(2, 4)):
            f.write(f"- {fake.sentence()}\n")
        f.write("\n")
        f.write("## Risoluzione\n")
        f.write("Sequenza di ripristino:\n")
        for i in range(1, random.randint(3, 6)):
            f.write(f"{(i)}. {fake.sentence()}\n")
        f.write("\n")
        f.write("## Quando escalare\n")
        f.write(f"Se l'errore persiste: {fake.sentence()}\n")

def generate_reference(file_path, domain, feature):
    title = f"Riferimento Tecnico per {feature}"
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(generate_yaml_front_matter(title, "reference", domain, feature))
        f.write(f"# {title}\n\n")
        f.write("Specifiche tecniche.\n\n")
        f.write("## Campi\n")
        for _ in range(random.randint(2, 4)):
            f.write(f"### {fake.word().capitalize()}\n")
            f.write(f"**Tipo:** {random.choice(['String', 'Integer', 'Boolean'])}\n")
            f.write(f"**Descrizione:** {fake.sentence()}\n\n")
        f.write("## Regole\n")
        for _ in range(random.randint(2, 4)):
            f.write(f"### Regola {fake.word().capitalize()}\n")
            f.write(f"**Condizione:** {fake.sentence()}\n")
            f.write(f"**Validazione:** {fake.paragraph()}\n\n")

def main():
    parser = argparse.ArgumentParser(description="Generate synthetic Markdown knowledge base files.")
    parser.add_argument("--count", type=int, default=50, help="Number of files to generate")
    parser.add_argument("--outdir", type=str, default="mock_knowledge_base", help="Output directory")
    args = parser.parse_args()

    generators = [
        ("how_to", generate_how_to),
        ("troubleshooting", generate_troubleshooting),
        ("reference", generate_reference)
    ]
    
    print(f"Generating {args.count} mock documents in '{args.outdir}'...")
    features = ["auth", "report", "database", "ui", "export"]
    
    for i in range(args.count):
        doc_kind, generator_func = random.choice(generators)
        domain = random.choice(ERP_MODULES).lower().replace(" ", "_")
        feature = random.choice(features)
        
        # Le cartelle devono rispettare layout v2: outdir/<domain>/<feature>/<doc_kind>/
        target_dir = os.path.join(args.outdir, domain, feature, doc_kind)
        os.makedirs(target_dir, exist_ok=True)
        
        filename = f"{doc_kind}_{fake.uuid4()[:8]}.md"
        file_path = os.path.join(target_dir, filename)
        generator_func(file_path, domain, feature)
        
    print(f"✅ Fatto! Generati {args.count} file in {args.outdir}")

if __name__ == "__main__":
    main()
